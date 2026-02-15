import streamlit as st
from openai import OpenAI

# -------------------------------------------------
# Configuration
# -------------------------------------------------
st.set_page_config(page_title="Personality Selector", page_icon="🧠")
st.title("🧠 Personality Selector Chatbot")

# -------------------------------------------------
# Initialize OpenRouter client (API key via secrets or sidebar input)
# -------------------------------------------------
if "OPENROUTER_API_KEY" in st.secrets:
    api_key = st.secrets["OPENROUTER_API_KEY"]
else:
    api_key = st.sidebar.text_input("Enter OpenRouter API Key", type="password")

if not api_key:
    st.warning("Please provide an OpenRouter API key.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Personality Selector",
    },
)

# -------------------------------------------------
# Personality definitions
# -------------------------------------------------
PERSONALITIES = {
    "Professional Business Assistant": {
        "system_prompt": (
            "You are a professional business assistant. "
            "Respond in a formal, structured manner, focusing on business strategy and professional communication. "
            "Be polite, efficient, and results‑oriented."
        )
    },
    "Creative Writing Helper": {
        "system_prompt": (
            "You are a creative writing helper. "
            "Respond with imaginative, expressive language, encouraging storytelling and artistic ideas. "
            "Use an enthusiastic and artistic tone."
        )
    },
    "Technical Expert": {
        "system_prompt": (
            "You are a technical expert. "
            "Provide precise, detailed, code‑focused explanations. "
            "Use an analytical, methodical style suitable for programming problems."
        )
    },
    "Friendly Companion": {
        "system_prompt": (
            "You are a friendly companion. "
            "Chat in a warm, supportive, conversational tone. "
            "Offer casual advice and emotional support when appropriate."
        )
    },
}

# -------------------------------------------------
# Sidebar UI – personality selection
# -------------------------------------------------
with st.sidebar:
    st.header("Settings")
    selected_personality = st.selectbox(
        "Choose personality",
        options=list(PERSONALITIES.keys()),
        index=0,
    )
    st.caption(f"Current: **{selected_personality}**")

# -------------------------------------------------
# Session state initialisation
# -------------------------------------------------
if "personality" not in st.session_state:
    st.session_state.personality = selected_personality
    # Insert initial system message according to the chosen personality
    st.session_state.messages = [
        {"role": "system", "content": PERSONALITIES[selected_personality]["system_prompt"]}
    ]
else:
    # Detect personality change and reset system prompt accordingly
    if st.session_state.personality != selected_personality:
        st.session_state.personality = selected_personality
        # Replace the first message (system) with the new prompt
        if st.session_state.messages and st.session_state.messages[0]["role"] == "system":
            st.session_state.messages[0]["content"] = PERSONALITIES[selected_personality]["system_prompt"]
        else:
            st.session_state.messages.insert(0, {"role": "system", "content": PERSONALITIES[selected_personality]["system_prompt"]})

# -------------------------------------------------
# Display chat history
# -------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])
    # system messages are not shown to the user

# -------------------------------------------------
# Handle new user input
# -------------------------------------------------
if user_input := st.chat_input("Ask something …"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare request to OpenRouter – include the whole message list
    # Assistant response handling – accumulate streamed chunks and render once within a chat_message container
    try:
        response = client.chat.completions.create(
            model="arcee-ai/trinity-large-preview:free",
            messages=st.session_state.messages,
            stream=True,
            extra_headers={
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": f"{selected_personality} Chat",
            },
            extra_body={"provider": {"data_collection": "deny"}},
        )
        full_reply = ""
        # Stream chunks and update UI incrementally
        with st.chat_message("assistant"):
            placeholder = st.empty()
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    full_reply += content
                    placeholder.markdown(full_reply, unsafe_allow_html=False)
        # Store assistant reply
        st.session_state.messages.append({"role": "assistant", "content": full_reply})
    except Exception as e:
        with st.chat_message("assistant"):
            st.error(f"Chat failed: {str(e)}")
            st.info("Try again or check your API key.")
