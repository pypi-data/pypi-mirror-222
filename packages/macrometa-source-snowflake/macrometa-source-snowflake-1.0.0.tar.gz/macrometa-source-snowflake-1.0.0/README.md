# macrometa-source-snowflake

A macrometa source that extracts data from a [Snowflake](https://www.snowflake.com/) database and produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

## How to use it

TODO: Add proper context
If you want to run this macrometa-source-snowflake connector independently please read further.

### Install and Run

First, make sure Python 3 is installed on your system or follow these
installation instructions for [Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/) or
[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04).
It's recommended to use a virtualenv:

```bash
make venv
```

### Configuration

1. Create a `config.json` file with connection details to snowflake, here is a [sample config file](./config_sample.json).
   **Note**: `table` is a mandatory parameter as well to avoid a long-running catalog discovery process.
   Please specify fully qualified table and view names and only that ones that you need to extract otherwise you can
   end up with very long running discovery mode of this source connector. Discovery mode is analysing table structures but
   Snowflake doesn't like selecting lot of rows from `INFORMATION_SCHEMA` or running `SHOW` commands that returns lot of
   rows. Please be as specific as possible.
2. Run it in discovery mode to generate a `properties.json`
3. Edit the `properties.json` and select the streams to replicate
4. Run the source connector like any other singer compatible tap:

```
  macrometa-source-snowflake --config config.json --properties properties.json --state state.json
```

### Authentication Methods

You can either use basic user/password authentication or Key Pair authentication.

#### User / Password authentication

Populate `user` and `password` in the `config.json` file

#### Key Pair authentication

To use key pair authentication, omit the `password` and instead provide the `private_key` to the unencrypted version of the private key and, optionally, the `private_key_passphrase`.

### Discovery mode

The macrometa-source-snowflake connector can be invoked in discovery mode to find the available table and columns in the database:

```bash
$ macrometa-source-snowflake --config config.json --discover
```

A discovered catalog is output, with a JSON-schema description of each table. A
source table directly corresponds to a Singer stream.

## Replication methods

The two ways to replicate a given table are `FULL_TABLE` and `LOG_BASED`.

### Full Table

Full-table replication extracts all data from the source table each time the connector
is invoked.

### LogBased

Macrometa source Snowflake connector can be used as a CDC (Change Data Capture) connector by specifying the Replication Method as LOG_BASED to capture any changes done at source and identify what records were inserted or updated or deleted, it will extract first all the records (i.e. FULL_TABLE) and then it will continuously listen to a Stream created on the Table to extract only the changes done.

### To run tests:

1. Define environment variables that requires running the tests

```
  export MACROMETA_SOURCE_SNOWFLAKE_ACCOUNT=<snowflake-account-name>
  export MACROMETA_SOURCE_SNOWFLAKE_DBNAME=<snowflake-database-name>
  export MACROMETA_SOURCE_SNOWFLAKE_USER=<snowflake-user>
  export MACROMETA_SOURCE_SNOWFLAKE_PASSWORD=<snowflake-password>
  export MACROMETA_SOURCE_SNOWFLAKE_PRIVATE_KEY=<snowflake-pk-path>
  export MACROMETA_SOURCE_SNOWFLAKE_PRIVATE_KEY_PASSPHRASE=<snowflake-passphrase>
  export MACROMETA_SOURCE_SNOWFLAKE_WAREHOUSE=<snowflake-warehouse>
```

2. Install python dependencies

```bash
make venv
```

3. To run unit tests:
   **PS**: There are no unit tests at the time of writing this document

```bash
make unit_test
```

4. To run Integration tests

```bash
make integration_test
```

### To run formatting and linting:

```bash
make venv format pylint
```

## License

Apache License Version 2.0
See [LICENSE](LICENSE) to see the full text.
