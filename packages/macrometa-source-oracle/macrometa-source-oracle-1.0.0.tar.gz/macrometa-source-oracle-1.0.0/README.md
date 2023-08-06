# macrometa-source-oracle

Macrometa source connector that extracts data from a [Oracle](https://www.oracle.com/database/) database and produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

## How to use it

### Install and Run

First, make sure Python 3 is installed on your system or follow these
installation instructions for [Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/) or
[Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04).


It's recommended to use a virtualenv:

```bash
  python3 -m venv venv
  pip install macrometa-source-oracle
```

or from source using,
1. Install poetry using https://python-poetry.org/docs/#installation
2. Run 
    ```bash
    poetry build
    pip install dist/macrometa_source_oracle-<version>*.whl
    ```

### Configuration

Running the the macrometa source connector independently requires a `config.json` file. 

Example configuration:

```json
{
  "host": "dev.oracledb.io",
  "port": 1521,
  "user": "C##HELLO",
  "password": "password",
  "service_name": "ORCLCDB",
  "filter_schema": "C##HELLO",
  "filter_table": "CUSTOMERS",
  "replication_method": "LOG_BASED",
  "pdb_name": "ORCLPDB1",
  "multitenant": true,
  "scn_window_size": 10
}
```

You can run a discover run using the previous `config.json` file to acquire all the tables definition
 
```
macrometa-source-oracle --config /tmp/config.json --discover >> /tmp/catalog.json
```

Then use the catalog.json to run a full export:

```
macrometa-source-oracle --config /tmp/config.json --catalog /tmp/catalog.json
```

