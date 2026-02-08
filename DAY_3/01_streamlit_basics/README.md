# Streamlit Basics

This directory contains a series of small Streamlit applications that demonstrate common patterns and features of the Streamlit framework.  The examples are designed to be run one‑off scripts using `streamlit run <script>.py`.

---

## Files Overview

| File | Description |
|------|-------------|
| `00_streamlit_app.py` | Minimal hello‑world Streamlit app. Shows the most basic `st.title` and `st.write` usage. |
| `01_hello_world.py` | A slightly more elaborate example with text input and button interactions. |
| `02_session_state.py` | Demonstrates how to persist data across reruns using `st.session_state`. |
| `03_chat_interface.py` | Implements a simple chat‑like interface with a text input box and message history. |
| `04_sidebar_widgets.py` | Shows how to place controls (sliders, selectboxes, etc.) in the Streamlit sidebar. |
| `05_complete_example.py` | A full‑featured example that ties together sidebar controls, session state, and a chat‑style UI. |
| `requirements.txt` | Pin‑points the exact Streamlit version used for these examples (and any other dependencies). |

---

## Getting Started

1. **Create/activate the Python environment** (if you haven't already):
   ```bash
   source .venv/bin/activate   # macOS / Linux
   # Or create a new virtual env if `.venv` does not exist
   python -m venv .venv && source .venv/bin/activate
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run an example**.  From this folder, execute:
   ```bash
   streamlit run 00_streamlit_app.py
   ```
   Then open the URL shown in the terminal (usually `http://localhost:8501`).

   Replace `00_streamlit_app.py` with any of the other files to explore different features.

---

## Tips & Common Patterns

- **Live reloading** – Streamlit automatically refreshes the UI when you save changes to the source file.
- **Session state** – Use `st.session_state` to store mutable data (e.g., a list of chat messages) that persists between reruns.
- **Sidebar** – The `st.sidebar` object mirrors the main API, allowing you to place widgets on the left panel.
- **Widgets** – Widgets return a value (e.g., `st.slider`, `st.selectbox`). Store the return in a variable and use it to drive the UI.

---

## Running All Examples Sequentially (Optional)

If you want to quickly see each demo one after another, you can use a simple bash loop:
```bash
for f in *.py; do
  echo "Running $f..."
  streamlit run "$f" &
  sleep 5   # give a few seconds to view the app
  pkill -f "streamlit run $f"   # stop the app
done
```

> **Note**: The loop above is for local experimentation only; it stops each app after a short pause.

---

## Contributing

Feel free to add new examples or improve existing ones.  When you create a new script, update the table above and add a short description.

---

*Generated with Claude Code*