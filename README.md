# AI Learning
![CI](https://github.com/raghu04/ai-accelerator/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Project Overview**
This repository contains a collection of interactive Jupyter notebooks that walk through Python and machine‑learning concepts, from basic data structures to multithreading, quantum‑compatible code, and generative AI demos. The notebooks are grouped by learning modules and sandbox experiments.

**Prerequisites**
- Python 3.10 or newer
- `pip` (installed with Python)
- `git` (to clone the repo)

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

- `Basecamp/Day_1` – Introductory notebooks covering Jupyter basics, Python fundamentals, environment setup, functions, classes, file handling, and AI model integrations.
  - `1_Jupyter.ipynb` – Intro to Jupyter notebooks.
  - `2_Python_Basics.ipynb` – Variables, data types, and basic operations.
  - `3_vEnV_Examples.ipynb` – Working with virtual environments.
  - `4_Functions.ipynb` – Defining and using functions.
  - `5_Class.ipynb` – Object‑oriented basics.
  - `6_Files.ipynb` – File I/O examples.
  - `7_Groq.ipynb` – Using the Groq LLM API.
  - `8_Gemini.ipynb` – Using the Gemini model.

- `Basecamp/Day_2` – Intermediate topics such as collections, tuples, dictionaries, strings, iterators, generators, exceptions, NumPy, and pandas.
  - `1_Lists.ipynb` – List basics.
  - `2_Lists.ipynb` – Advanced list operations.
  - `3_Tuples.ipynb` – Tuple usage.
  - `4_Dictionary.ipynb` – Dictionaries.
  - `5_Strings.ipynb` – String manipulation.
  - `6_Iter_n_Gen.ipynb` – Iterators and generators.
  - `7_Exceptions.ipynb` – Exception handling.
  - `8_Numpy.ipynb` – NumPy fundamentals.
  - `9_Pandas.ipynb` – Pandas data analysis.
  - `10_Thread.ipynb` – Threading basics.

- `DAY_1` – Sandbox for experimental notebooks.
  - `chat_completion.ipynb` – Demonstrates chat completion with LLMs.

- `DAY_2` – Additional sandbox experiments.
  - `Assignment.ipynb` – Sample assignment tasks.
  - `Gradio.ipynb` – Simple Gradio UI demo.
  - `Hugging_face.ipynb` – Using Hugging Face models.

- `DAY_3` – Sandbox containing Streamlit examples, ChatGPT app, and assignment notebooks.
- `DAY_4` – JSON configuration files for linked job automation and personal newsletter.
- `DAY_5` – JSON files for n8n LinkedIn post creator, Prompt App, and video resume coverletter.

- `CLAUDE.md` – Guidance for Claude Code when interacting with the repository.
- `.github/workflows/ci.yml` – GitHub Actions CI that runs the notebooks to verify they execute without errors.

## Contact
Maintainer: **Raghu S** – [GitHub profile](https://github.com/raghu04)
For questions or issues, open a GitHub Issue or use the repository’s Discussions.

---
*Happy coding and learning!*