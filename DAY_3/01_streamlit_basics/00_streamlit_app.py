import streamlit as st

# Define the pages
hello_world = st.Page("01_hello_world.py", title="Hello World", icon="👋")
session_state = st.Page("02_session_state.py", title="Session State", icon="🧠")
chat_interface = st.Page("03_chat_interface.py", title="Chat Interface", icon="💬")


# Set up the navigation
pg = st.navigation([hello_world, session_state, chat_interface])

# Render the selected page
pg.run()