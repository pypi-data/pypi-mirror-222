# Pomatillo

## Introduction

Pomatillo is a simple Pomodoro timer for the command line. It is meant to be used in the
following modes:

- As a library for other programs
- As a command line tool (CLI)
- As a Textual User Interface (TUI)

Other modes may be added upon request.

## Installation

Pomatillo supports Python 3.10 and above. To install Pomatillo, run the following command:

```bash
pip install pomatillo
```

## Development

Pomatillo uses [Poetry](https://python-poetry.org/) for dependency management and packaging.
If you want to contribute to Pomatillo, here are the steps to get started:

```bash
# Clone the repo
git clone https://github.com/AdityaGudimella/pomatillo
# Go into the repo
cd pomatillo
# Install dependencies using Poetry
poetry install
```

## Running tests

Pomatillo uses [pytest](https://docs.pytest.org/en/stable/) for testing. To run the
tests, run the following command:

### Using a Poetry managed virtual environment

```bash
poetry run pytest
```

### If you installed it in a custom managed virtual environment

Activate the virtual environment and run the following command:

```bash
python -m pytest
```

## Building docs

Pomatillo uses [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) for
documentation. To help with various documentation tasks, Pomatillo provides a cli:

- Using a Poetry managed virtual environment

```bash
poetry run pomatillo docs --help
```

- If you installed it in a custom managed virtual environment, activate the virtual
  environment first

```bash
python -m pomatillo docs --help
```
