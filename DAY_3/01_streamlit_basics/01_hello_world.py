"""
Example 1: Hello World - Understanding Script Execution
"""

import streamlit as st

st.title("👋 Understanding Script Execution")

# This runs every time the app loads or user interacts
st.write("🌍 Hello Streamlit World!")

st.write("This text appears every time the script runs.")

# Adding a button to demonstrate reruns
if st.button("Click Me!"):
    st.write("🎉 Button was clicked! The entire script just ran again.")
    st.balloons()

# Add a text input to show interactive reruns
name = st.text_input("What's your name:")
if name:
    st.write(f"👋 Hello, {name}! The script ran again when you entered your name.")

# Add a counter to show state persistence across reruns
st.write("---")
st.write("**Script Execution Counter:**")
st.write("Every time you see this number change, the entire script ran from top to bottom.")

# This would reset to 0 every time without session state, but we can use session state to persist it
if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.write(f"Script has run {st.session_state.counter} times.")

# Expanders to show the code execution flow
with st.expander("See the code execution flow"):
    st.write("""
    1. The script starts executing from the top.
    2. Each widget (button, text input) triggers a complete rerun of the script.
    3. The session state allows us to persist data across these reruns.
    4. This model is different from traditional web frameworks where you might have event handlers that only run specific code.
    """)
