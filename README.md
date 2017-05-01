# Beamin target

This is intended to be used with the Beamin controller for managing Info-Beamer instances running on many systems.  It is currently only compatible with Python 3.  Use pip/pip3 to install.

## Run

Start the server using `beamin_target`.

## Configuration

The `beamin_target` command requires a `config.json` file in the current directory.

```json
{
  "info_beamer_cmd": "info-beamer",
  "raspberry_pi": true
}
```

This can call info-beamer if it is not in your path:

```json
{
  "info_beamer_cmd": "/home/pi/info-beamer-pi/info-beamer",
  "raspberry_pi": true
}
```
