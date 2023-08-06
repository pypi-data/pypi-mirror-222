# swagd

Swagger UI Server for debugging purpose.

## Install

```shell
pip install swagd
```

## Usage

Go to the directory containing openapi files. Run `swagd` to start the Swagger UI server:

```
swagd 8090
```

The port number is optional. See the python module `http.server` for supported arguments.

```shell
usage: swagd [-h] [-b ADDRESS] [-d DIRECTORY] [-p VERSION] [port]

positional arguments:
  port                  bind to this port (default: 8000)

options:
  -h, --help            show this help message and exit
  -b ADDRESS, --bind ADDRESS
                        bind to this address (default: all interfaces)
  -d DIRECTORY, --directory DIRECTORY
                        serve this directory (default: current directory)
  -p VERSION, --protocol VERSION
                        conform to this HTTP version (default: HTTP/1.0)
```