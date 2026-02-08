import streamlit as st

# Page configuration
st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded"
)

# Define the pages
hello_world = st.Page("01_hello_world.py", title="Hello World", icon="👋")
session_state = st.Page("02_session_state.py", title="Session State", icon="🧠")
chat_interface = st.Page("03_chat_interface.py", title="Chat Interface", icon="💬")
sidebar_widgets = st.Page("04_sidebar_widgets.py", title="Sidebar Widgets", icon="⚙️")
complete_example = st.Page("05_complete_example.py", title="Complete Example", icon="🚀")

# Set up the navigation
pg = st.navigation(
    [hello_world, session_state, chat_interface, sidebar_widgets, complete_example], 
    position="top"
)

# Render the selected page
pg.run()