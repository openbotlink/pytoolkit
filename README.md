# pytoolkit

`pytoolkit` is a small collection of helper modules that can be used across different Python projects.

The focus is on simple building blocks: configuration handling, logging, timing, HTTP helpers, caching, string helpers, and more.

Current version: **0.2.0**

## Project goals

- Provide small, composable utilities instead of a heavy framework
- Keep dependencies minimal and well known
- Make it easy to reuse the same helpers across many projects
- Stay readable and beginner friendly while still being robust

## Installation

From a local checkout:

```bash
pip install -e .
```

## Usage overview

The package is split into focused modules:

- `config_loader` for configuration loading
- `logger` for logging helpers
- `timer` for timing and profiling
- `http_client` for HTTP access
- `crypto_utils` for hashing and token generation
- `file_utils` for file handling
- `cache` for in memory caching
- `retry` for retry decorators
- `validators` for common validation helpers
- `math_tools` for small numeric helpers
- `string_tools` for text processing
- `task_scheduler` for recurring jobs
- `env` for environment handling
- `cli` for building command line interfaces
- `context_utils` for working with nested dictionaries
- `serialization` for JSON / YAML / TOML helpers

See the `examples` directory for small, complete scripts.

## CLI

After installation a small CLI entry point is available:

```bash
pytoolkit info
pytoolkit env
```

Use `pytoolkit --help` to see available commands.

## Contributing

- Fork the repository
- Create a new branch for your change
- Add or adjust tests where it makes sense
- Run the test suite:

```bash
python -m unittest discover -s tests
```

- Open a pull request with a short description of your change

## Versioning

The project follows a simple semantic versioning scheme:

- Breaking changes bump the **major** version
- New features bump the **minor** version
- Small fixes bump the **patch** version

## Changelog (short)

- **0.2.0**
  - Added context and serialization helpers
  - Extended CLI with more commands
  - Added more tests
  - Added GitHub Actions workflow for linting and tests

For details see the source files.
