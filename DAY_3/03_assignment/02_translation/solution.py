import streamlit as st
from openai import OpenAI

# Configure the page
st.set_page_config(page_title="Translation Assistant", page_icon="🌐")

# Page title
st.title("🌐 Translation Assistant")

# Initialize the OpenAI client with OpenRouter
if "OPENROUTER_API_KEY" in st.secrets:
    api_key = st.secrets["OPENROUTER_API_KEY"]
else:
    api_key = st.sidebar.text_input("Enter OpenRouter API Key", type="password")

if not api_key:
    st.warning("Please enter your OpenRouter API key to continue.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Translation Assistant",
    }
)

# Sidebar for language selection
with st.sidebar:
    st.header("Settings")

    target_language = st.selectbox(
        "Target Language:",
        ["English", "Spanish", "French", "German", "Chinese", "Japanese"],
    )

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []


if user_input := st.chat_input("Enter text to translate:"):
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
    Translate this text to {target_language}: "{user_input}"

    Respond in JSON format:
    {{
        "detected_language": "language name",
        "translation": "translated text",
        "confidence": "high/medium/low"
    }}
    """

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="arcee-ai/trinity-large-preview:free",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream=True,
                extra_headers={
                    "HTTP-Referer": "http://localhost:8501",
                    "X-Title": "My ChatBot"
                },
                extra_body={
                    "provider": {
                        "data_collection": "deny"  # or "allow" if you permit retention
                    }
                }
            )

            # Initialize an empty string to collect the full response
            full_response = ""

            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    
            st.markdown(full_response)
            # st.markdown(f"""**Translation Result:**\n\n
            #             ```json\n
            #             Detected Language: {full_response['detected_language']}\n
            #             Translation: {full_response['translation']}\n
            #             Confidence: {full_response['confidence']} ̰\n
            #             ```
            #             """)

            
        except Exception as e:
            st.error(f"Translation failed: {str(e)}")
            st.info("Please try again with different text.")