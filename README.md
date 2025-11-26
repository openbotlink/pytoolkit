# pytoolkit

`pytoolkit` is a small collection of helper modules that can be used across different Python projects.

The focus is on simple building blocks: configuration handling, logging, timing, HTTP helpers, caching, string helpers, and more.

Current version: **0.1.1**

## Features

- Configuration loader for `.env`, JSON, YAML and TOML files
- Structured logging with optional colored output
- Logging configuration helper that can read log level from environment variables
- Timing utilities for profiling functions and code blocks
- Thin HTTP client wrapper on top of `requests`, usable as a context manager
- Crypto helpers for hashing and token generation
- File helpers for reading, writing and hashing files
- In memory caching utilities and a `@cached` decorator that correctly handles `None`
- Simple retry decorators for unreliable operations
- Small validation helpers for common data types
- String and math helper functions
- Lightweight task scheduler for recurring jobs with basic error logging
- CLI helper for building command line interfaces and a small built in `info` command
- Environment handling for separating development, staging and production

## Installation

You can install the package from a local checkout:

```bash
pip install -e .
```

or build a wheel and install that:

```bash
python -m build
pip install dist/pytoolkit-0.1.1-py3-none-any.whl
```

## Quick start

Here is a minimal example that combines several utilities:

```python
from pytoolkit.logger import configure_from_env
from pytoolkit.config_loader import ConfigLoader
from pytoolkit.timer import time_function
from pytoolkit.http_client import HttpClient

logger = configure_from_env()

config = ConfigLoader(
    env_file=".env",
    json_file="config.json",
)

@time_function(logger=logger)
def fetch_status():
    with HttpClient() as client:
        response = client.get("https://httpbin.org/status/200")
    return response.status_code

if __name__ == "__main__":
    logger.info("Loaded config: %s", config.as_dict())
    status = fetch_status()
    logger.info("HTTP status code: %s", status)
```

More examples can be found in the `examples` directory.

## CLI

After installing the package you can use the small command line interface:

```bash
pytoolkit info
```

This prints a short message and verifies that the package and CLI wiring are working.

## Modules overview

(unchanged, see file for full descriptions)

## Testing

Tests are in the `tests` directory and use the standard `unittest` library.

```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT license. See the `LICENSE` file for details.
