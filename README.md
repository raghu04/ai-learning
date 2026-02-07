# AI Learning

This repository is a collection of learning notebooks that explore Python and machine‑learning concepts.  The code lives primarily in Jupyter notebooks, with a few supporting scripts.

## Getting Started

1. **Set up the virtual environment** (if not already present):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Launch Jupyter** to work with the notebooks:
   ```bash
   jupyter notebook
   ```

3. **Run a notebook from the command line** (useful for CI or batch runs):
   ```bash
   jupyter nbconvert --to notebook --execute "Basecamp/Day_1/1_Jupyter.ipynb" --output /dev/null
   ```
   Replace the path with the notebook you wish to execute.

## Repository Structure

- `Basecamp/Day_1` – Introductory material (variables, data structures, functions).
- `Basecamp/Day_2` – Intermediate topics (iterators, generators, concurrency, etc.).
- `DAY_1` – Sandbox folder containing experimental notebooks such as `Chat_completion.ipynb`.
- `DAY_2` – Sandbox folder containing experimental notebooks such as `Gradio.ipynb`.
- `CLAUDE.md` – Guidance for Claude Code when interacting with the repo.
- `.github/workflows/ci.yml` – GitHub Actions CI that runs `black`, `flake8`, and executes every notebook to verify they run without errors.

---
*Happy coding and learning!*