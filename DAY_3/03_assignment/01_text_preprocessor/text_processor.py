import streamlit as st
import textwrap

# Page configuration
st.set_page_config(page_title="Interactive Text Processor", page_icon="📝", layout="centered")

# Title and subtitle
st.title("Interactive Text Processor")
st.subheader("A simple Streamlit app to explore basic text processing operations")

# ---- Sidebar configuration ----
st.sidebar.header("Configuration")
process_type = st.sidebar.selectbox(
    "Select processing type",
    ["Word Count", "Character Count", "Reverse Text", "Uppercase", "Title Case"],
    help="Choose how to transform the input text.",
)
char_limit = st.sidebar.number_input(
    "Character limit",
    min_value=10,
    max_value=500,
    value=100,
    help="Maximum number of characters allowed in the input.",
)
show_steps = st.sidebar.checkbox("Show processing steps", value=False)

# ---- Theme selection ----
theme = st.sidebar.selectbox("Select theme", ["Light", "Dark"], help="Choose light or dark theme for result display")

# ---- Main input area ----
user_input = st.text_area(
    "Enter text",
    height=200,
    help=textwrap.dedent(
        """Type or paste the text you want to process.
        The app will respect the character limit set in the sidebar.
        """
    ),
)

# Input validation
if user_input:
    if len(user_input) > char_limit:
        st.warning(f"Input exceeds the character limit of {char_limit} characters. It will be truncated for processing.")
        processed_input = user_input[:char_limit]
    else:
        processed_input = user_input
else:
    processed_input = ""

# ---- Processing functions ----
def word_count(text: str) -> str:
    words = text.split()
    return f"Word count: {len(words)}"

def char_count(text: str) -> str:
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", ""))
    return f"Characters (incl. spaces): {with_spaces}\nCharacters (no spaces): {without_spaces}"

def reverse_text(text: str) -> str:
    return text[::-1]

def uppercase(text: str) -> str:
    return text.upper()

def title_case(text: str) -> str:
    return text.title()

# ---- Mapping of processing type to function ----
process_funcs = {
    "Word Count": word_count,
    "Character Count": char_count,
    "Reverse Text": reverse_text,
    "Uppercase": uppercase,
    "Title Case": title_case,
}

# ---- Session state for processing history (last 3) ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Perform processing when there is input ----
if processed_input:
    func = process_funcs[process_type]
    result = func(processed_input)
    # Store in history (keep last 3)
    st.session_state.history.insert(0, {"type": process_type, "result": result})
    st.session_state.history = st.session_state.history[:3]

    # Display processing steps if requested
    with st.container():
        if show_steps:
            st.info("**Processing steps**")
            st.write(f"**Selected operation:** {process_type}")
            st.write(f"**Original text (truncated):** {processed_input}")
        # Styled output container
        if theme == "Dark":
            # Dark theme colors (darker backgrounds, white text)
            if process_type == "Word Count":
                out_color = "#263238"
            elif process_type == "Character Count":
                out_color = "#37474F"
            elif process_type == "Reverse Text":
                out_color = "#4527A0"
            elif process_type == "Uppercase":
                out_color = "#2E7D32"
            else:
                out_color = "#424242"
            text_color = "#FFFFFF"
        else:
            # Light theme (original pastel colors, dark text)
            if process_type == "Word Count":
                out_color = "#e0f7fa"
            elif process_type == "Character Count":
                out_color = "#fff3e0"
            elif process_type == "Reverse Text":
                out_color = "#f3e5f5"
            elif process_type == "Uppercase":
                out_color = "#e8f5e9"
            else:
                out_color = "#eceff1"
            text_color = "#000000"
        st.markdown(
            f"<div style='background:{out_color}; color:{text_color}; padding:15px; border-radius:5px; margin-bottom:15px'>" +
            f"<h4 style='margin:0;'>Result</h4><p>{result.replace('\n','<br>')}</p></div>",
            unsafe_allow_html=True,
        )
        st.success("Processing complete!")
        # Download button
        st.download_button(
            label="Download result",
            data=result.encode("utf-8"),
            file_name="processed_text.txt",
            mime="text/plain",
        )
else:
    st.info("Enter some text above to see processing results.")

# ---- Display processing history ----
if st.session_state.history:
    st.sidebar.header("Processing History (last 3)")
    for entry in st.session_state.history:
        st.sidebar.write(f"* {entry['type']}: {entry['result'][:30].replace('\n',' ')}...")
