# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of Jupyter notebooks that walk through various concepts in Python and machine‑learning, including
- basic data structures
- numerical libraries (NumPy, pandas)
- multithreading,
- quantum‑compatible code, etc.

The repository does not contain a conventional Python package or test suite.  Development mainly consists of creating, editing, and executing notebooks.

## Common Development Tasks

### 1.  Launch the Notebooks Session
```bash
# Activate the Python environment (if not already active)
source .venv/bin/activate  # on macOS / Linux
# Start Jupyter server
jupyter notebook
```

The server will open a browser window pointing to `http://localhost:8888`.  The most recent notebooks live under `Basecamp/Day_1` and `Basecamp/Day_2`.

### 2. Run a Single Notebook
From the Jupyter UI you can select a notebook and run all kernels or particular cells.  Alternatively, you can run a notebook from the command line with `nbconvert`:
```bash
jupyter nbconvert --execute "Basecamp/Day_1/1_Jupyter.ipynb" --to notebook
```

### 3.  Work With the Virtual Environment
The repository ships with a pre‑built `.venv` directory containing site‑packages.  If you need to manage packages or re‑install dependencies you can run:
```bash
source .venv/bin/activate
pip install -r requirements.txt    # if a requirements file exists
```

### 4.  Commit and Push Changes
```bash
git add <changed_notebooks>
# Provide a concise message that explains the notebook changes
git commit -m "Update Day 2: Fixed a typo in 5_Strings.ipynb"
# Push to the remote (anonymized token is not included here)
git push
```

## High‑Level Architecture

The repository is organized around *learning modules*.

- **Basecamp/Day_1** – Introductory material: variables, data types, functions.
- **Basecamp/Day_2** – Deeper concepts: iterators, generators, concurrency.
- **DAY_2** – A quick sandbox that demonstrates a Gradio interface.

Each notebook is largely self‑contained; code is not imported across notebooks.  If a notebook creates functions that will be reused later, the author typically copies the snippet into another notebook rather than importing from a shared module.

## Helpful Resources

- `jupyter --help` – see learning commands for Jupyter.
- `pip list` – inspect available packages in the environment.
- `git log --oneline` – view concise commit history.

Feel free to tweak these instructions to suit your workflow.  Happy coding!
