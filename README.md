# variant-pipeline

A backend pipeline for genomic variant analysis. It parses VCF files containing germline small variants (SNVs, MNVs and small indels), stores variants and per-sample calls in PostgreSQL, annotates them from ClinVar and dbSNP with the source and retrieval time recorded, and exposes the results through a REST API.

## Status

Early development (Phase 0). The project skeleton is being set up. There is no working code yet.

## Requirements

- Python 3.12 or newer
- Git
- Developed and tested on Ubuntu 24.04 under WSL2. Other Linux distributions and macOS should work but are untested.

On Ubuntu, creating a virtual environment may need the `python3-venv` package:

    sudo apt install python3-venv

## Setup

Clone the repository and enter it:

    git clone https://github.com/ammaryh92/variant-pipeline.git
    cd variant-pipeline

Create a virtual environment in `.venv` and activate it:

    python3 -m venv .venv
    source .venv/bin/activate

Your prompt now starts with `(.venv)`. Activate it again in every new terminal before working on the project.

Install the package in editable mode, with the development tools:

    python -m pip install -e ".[dev]"

Editable mode means changes to the code in `src/` take effect without reinstalling. Reinstall only after changing `pyproject.toml`.

## Running the checks

From the project root, with the virtual environment active:

    pytest
    mypy src tests

Both should pass with no errors.

## License

MIT. See [LICENSE](LICENSE).
