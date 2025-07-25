# marimo-demo

Examples of using [marimo](https://marimo.io/) notebooks. This repository is heavily inspired by the official [usage examples](https://docs.marimo.io/examples/) in the docs and [examples](https://github.com/marimo-team/marimo/tree/main/examples) in the marimo repository.

> [!IMPORTANT]
> `uv` is the preferred python environment and package manager ([install docs](https://github.com/astral-sh/uv/?tab=readme-ov-file#installation)). While marimo supports all major package managers, it integrates especially tightly with uv ([docs](https://docs.marimo.io/guides/package_management/using_uv/)).

## Running notebooks

### `uv`

```bash
uvx marimo tutorial intro
uvx marimo tutorial --help
uvx marimo edit --sandbox my_notebook.py
```

> [!TIP]
> The [`--sandbox` flag](https://docs.marimo.io/guides/package_management/inlining_dependencies/) opens the notebook in an isolated virtual environment,
> automatically installing the notebook's dependencies 📦

### Virtual environment

```bash
# setup
uv venv
uv sync requirements.txt
source .venv/bin/activate
# use
marimo tutorial intro
marimo edit my_notebook.py
```

### VS Code extension

1. Install the [marimo VS Code extension](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)
2. Use the extension to edit and run notebooks directly from VS Code

### molab

[molab](https://molab.marimo.io/notebooks) is a free cloud-hosted marimo notebook workspace.

## Updating virtual environment packages

1. Edit `requirements.in`
2. Run `uv pip compile requirements.in -o requirements.txt`
3. Run `uv sync requirements.txt`
