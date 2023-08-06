#!/usr/bin/env python3
# pylint: disable=too-many-arguments,duplicate-code,too-many-locals

import copy
import datetime
import singer
import time
import uuid

import singer.metrics as metrics
from singer import metadata
from singer import utils

LOGGER = singer.get_logger('macrometa_source_snowflake')


def escape(string):
    """Escape strings to be SQL safe"""
    if '"' in string:
        raise Exception("Can't escape identifier {} because it contains a backtick"
                        .format(string))
    return '"{}"'.format(string)


def generate_tap_stream_id(catalog_name, schema_name, table_name):
    """Generate tap stream id as appears in properties.json"""
    return catalog_name + '-' + schema_name + '-' + table_name


def get_stream_version(tap_stream_id, state):
    """Get stream version from bookmark"""
    stream_version = singer.get_bookmark(state, tap_stream_id, 'version')

    if stream_version is None:
        stream_version = int(time.time() * 1000)

    return stream_version


def stream_is_selected(stream):
    """Detect if stream is selected to sync"""
    md_map = metadata.to_map(stream.metadata)
    selected_md = metadata.get(md_map, (), 'selected')

    return selected_md


def property_is_selected(stream, property_name):
    """Detect if field is selected to sync"""
    md_map = metadata.to_map(stream.metadata)
    return singer.should_sync_field(
        metadata.get(md_map, ('properties', property_name), 'inclusion'),
        metadata.get(md_map, ('properties', property_name), 'selected'),
        True)


def get_database_name(catalog_entry):
    """Get database name from catalog"""
    md_map = metadata.to_map(catalog_entry.metadata)

    return md_map.get((), {}).get('database-name')


def get_schema_name(catalog_entry):
    """Get schema name from catalog"""
    md_map = metadata.to_map(catalog_entry.metadata)

    return md_map.get((), {}).get('schema-name')


def get_key_properties(catalog_entry):
    """Get key properties from catalog"""
    catalog_metadata = metadata.to_map(catalog_entry.metadata)
    stream_metadata = catalog_metadata.get((), {})

    return stream_metadata.get('table-key-properties', [])


def insert_into_stream_sql(catalog_entry, stream_name, columns, rows_saved):
    database_name = get_database_name(catalog_entry)
    schema_name = get_schema_name(catalog_entry)
    escaped_db = escape(database_name)
    escaped_schema = escape(schema_name)
    table_name = catalog_entry.table
    escaped_table = escape(table_name)

    column = columns[0]

    escaped_col = escape(column)

    property_format = None
    # fetch the column type format from the json schema alreay built
    property_format = catalog_entry.schema.properties[column].format

    # if the column format is binary, fetch the hexified value
    if property_format == 'binary':
        escaped_col = f'hex_encode({escaped_col}) as {escaped_col}'

    query = f"""
    INSERT INTO {escaped_db}.{escaped_schema}.{escaped_table} ({escaped_col})
    SELECT METADATA$ACTION FROM {stream_name}
    WHERE false LIMIT {rows_saved};
    """

    return query


def create_stream(catalog_entry):
    database_name = get_database_name(catalog_entry)
    schema_name = get_schema_name(catalog_entry)
    escaped_db = escape(database_name)
    escaped_schema = escape(schema_name)
    table_name = catalog_entry.table
    escaped_table = escape(table_name)
    unique_id = str(uuid.uuid4())[:16].replace('-', '_')
    stream_name = f"{table_name}_macrometa_{unique_id}"

    query = f"""
    CREATE OR REPLACE STREAM {escaped_db}.{escaped_schema}.{stream_name}
    ON TABLE {escaped_db}.{escaped_schema}.{escaped_table};
    """
    stream_exists_query = f"""
    SHOW STREAMS LIKE '{stream_name}' IN {escaped_db}.{escaped_schema};
    """

    return query, stream_name, stream_exists_query


def generate_select_sql(catalog_entry, columns, limit=None):
    """Generate SQL to extract data froom snowflake"""
    database_name = get_database_name(catalog_entry)
    schema_name = get_schema_name(catalog_entry)
    escaped_db = escape(database_name)
    escaped_schema = escape(schema_name)
    escaped_table = escape(catalog_entry.table)
    escaped_columns = []

    for col_name in columns:
        escaped_col = escape(col_name)

        property_format = None
        # fetch the column type format from the json schema alreay built
        if col_name not in ['METADATA$ACTION', 'METADATA$ISUPDATE']:
            property_format = catalog_entry.schema.properties[col_name].format

        # if the column format is binary, fetch the hexified value
        if property_format == 'binary':
            escaped_columns.append(
                f'hex_encode({escaped_col}) as {escaped_col}')
        else:
            escaped_columns.append(escaped_col)

    select_sql = f'SELECT {",".join(escaped_columns)} FROM {escaped_db}.{escaped_schema}.{escaped_table}'

    if limit:
        select_sql = f'{select_sql} LIMIT {limit}'
    # escape percent signs
    select_sql = select_sql.replace('%', '%%')
    return select_sql


def generate_delete_stream_sql(catalog_entry, stream_name):
    """Generate SQL to delete stream froom snowflake"""
    database_name = get_database_name(catalog_entry)
    schema_name = get_schema_name(catalog_entry)
    escaped_db = escape(database_name)
    escaped_schema = escape(schema_name)

    return f"""
    DROP STREAM IF EXISTS {escaped_db}.{escaped_schema}.{stream_name};
    """


# pylint: disable=too-many-branches
def row_to_singer_record(catalog_entry, version, row, columns, time_extracted, time_deleted=None, replication_method=None):
    """Transform SQL row to singer compatible record message"""
    row_to_persist = ()
    for idx, elem in enumerate(row):
        property_type = catalog_entry.schema.properties[columns[idx]].type
        if isinstance(elem, datetime.datetime):
            row_to_persist += (elem.isoformat() + '+00:00',)

        elif isinstance(elem, datetime.date):
            row_to_persist += (elem.isoformat() + 'T00:00:00+00:00',)

        elif isinstance(elem, datetime.timedelta):
            epoch = datetime.datetime.utcfromtimestamp(0)
            timedelta_from_epoch = epoch + elem
            row_to_persist += (timedelta_from_epoch.isoformat() + '+00:00',)

        elif isinstance(elem, datetime.time):
            row_to_persist += (str(elem),)

        elif isinstance(elem, bytes):
            # for BIT value, treat 0 as False and anything else as True
            if 'boolean' in property_type:
                boolean_representation = elem != b'\x00'
                row_to_persist += (boolean_representation,)
            else:
                row_to_persist += (elem.hex(),)

        elif 'boolean' in property_type or property_type == 'boolean':
            if elem is None:
                boolean_representation = None
            elif elem == 0:
                boolean_representation = False
            else:
                boolean_representation = True
            row_to_persist += (boolean_representation,)

        else:
            row_to_persist += (elem,)
    rec = dict(zip(columns, row_to_persist))

    if replication_method == 'LOG_BASED':
        rec['_sdc_deleted_at'] = time_deleted or None

    return singer.RecordMessage(
        stream=catalog_entry.stream,
        record=rec,
        version=version,
        time_extracted=time_extracted)


def whitelist_bookmark_keys(bookmark_key_set, tap_stream_id, state):
    """..."""
    for bookmark_key in [non_whitelisted_bookmark_key
                         for non_whitelisted_bookmark_key
                         in state.get('bookmarks', {}).get(tap_stream_id, {}).keys()
                         if non_whitelisted_bookmark_key not in bookmark_key_set]:
        singer.clear_bookmark(state, tap_stream_id, bookmark_key)


def write_schema_message(catalog_entry, bookmark_properties=None):
    key_properties = get_key_properties(catalog_entry)

    singer.write_message(singer.SchemaMessage(
        stream=catalog_entry.stream,
        schema=catalog_entry.schema.to_dict(),
        key_properties=key_properties,
        bookmark_properties=bookmark_properties
    ))


def sync_query(cursor, catalog_entry, state, select_sql, columns, stream_version, params, replication_method):
    """..."""
    LOGGER.info('Running %s', select_sql)
    cursor.execute(select_sql, params)

    row = cursor.fetchone()
    rows_saved = 0

    database_name = get_database_name(catalog_entry)

    with metrics.record_counter(None) as counter:
        counter.tags['database'] = database_name
        counter.tags['table'] = catalog_entry.table
        time_deleted = None

        while row:
            time_extracted = utils.now()
            counter.increment()
            rows_saved += 1

            record_message = row_to_singer_record(catalog_entry,
                                                  stream_version,
                                                  row,
                                                  columns,
                                                  time_extracted,
                                                  time_deleted,
                                                  replication_method=replication_method)

            singer.write_message(record_message)

            md_map = metadata.to_map(catalog_entry.metadata)
            stream_metadata = md_map.get((), {})
            replication_method = stream_metadata.get(
                'replication-method', replication_method)

            if replication_method == 'FULL_TABLE':
                key_properties = get_key_properties(catalog_entry)

                if max_pk_values := singer.get_bookmark(
                    state, catalog_entry.tap_stream_id, 'max_pk_values'
                ):
                    last_pk_fetched = {k: v for k, v in record_message.record.items()
                                       if k in key_properties}

                    state = singer.write_bookmark(state,
                                                  catalog_entry.tap_stream_id,
                                                  'last_pk_fetched',
                                                  last_pk_fetched)

            if rows_saved % 1000 == 0:
                singer.write_message(singer.StateMessage(
                    value=copy.deepcopy(state)))

            row = cursor.fetchone()

    singer.write_message(singer.StateMessage(value=copy.deepcopy(state)))


def sync_log_based_query(connection, catalog_entry, state, select_sql, columns, stream_version, params, replication_method, stream_name=None):
    """..."""
    time_extracted = utils.now()

    rows = None
    rows_saved = 0
    try:
        cursor = connection.cursor()
        cursor.execute(select_sql, params)
        rows = cursor.fetchall()

        if not rows:
            connection.commit()
            time.sleep(10)
            return
        else:
            # Update stream offset to latest position by running a DML query
            cursor.execute(insert_into_stream_sql(catalog_entry, stream_name, columns, 1000))
            connection.commit()
    except Exception as e:
        connection.rollback()
        connection.cursor().execute(generate_delete_stream_sql(catalog_entry, stream_name))
        connection.commit()
        raise e

    database_name = get_database_name(catalog_entry)

    with metrics.record_counter(None) as counter:
        counter.tags['database'] = database_name
        counter.tags['table'] = catalog_entry.table
        time_deleted = None

        for row in rows:
            counter.increment()
            rows_saved += 1

            if len(row) > len(columns):  # Add this line to check if the row has metadata
                metadata_action = row[len(columns)]
                metadata_update = row[len(columns) + 1]

                row = row[:len(columns)]

                if metadata_action == 'DELETE':
                    if metadata_update:
                        continue
                    else:
                        time_deleted = singer.utils.strftime(utils.now())

            record_message = row_to_singer_record(catalog_entry,
                                                  stream_version,
                                                  row,
                                                  columns,
                                                  time_extracted,
                                                  time_deleted,
                                                  replication_method=replication_method)

            singer.write_message(record_message)

            if rows_saved % 1000 == 0:
                singer.write_message(singer.StateMessage(
                    value=copy.deepcopy(state)))

    singer.write_message(singer.StateMessage(value=copy.deepcopy(state)))
