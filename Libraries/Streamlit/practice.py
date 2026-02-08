import os
import streamlit as st
from google import genai

# -------------------- Page Config --------------------
st.set_page_config(page_title="IOAI Chat", page_icon="💬", layout="centered")
st.title("🤖 IOAI Practice Chat")
st.caption("Practice AI conversations using Google Gemini")

# -------------------- API Key Handling --------------------
# You can switch API keys here easily
api_keys = [
    "AIzaSyAi7CLrtHf4MZSn2rTEKd42jZYAR0rNl8E",
    "AIzaSyDnYWg263_XrTKOFw_pc7x3vdBTw5Blfq4"  # add more keys if needed
]

# Option to select which API key to use (0 = primary, 1 = secondary, etc.)
key_index = 0
api_key = api_keys[key_index]

if not api_key:
    st.error("❌ Missing GENAI_API_KEY. Set it directly in the code")
    st.stop()

# -------------------- Gemini Client --------------------
client = genai.Client(api_key=api_key)

# -------------------- Session State --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Chat History --------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------- Chat Input --------------------
prompt = st.chat_input("Ask anything for IOAI practice…")

if prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3-flash-preview",
                    contents=prompt
                )
                reply = response.text if hasattr(response, "text") else ""
            except Exception as e:
                # Suggest switching API key if quota exceeded
                if "RESOURCE_EXHAUSTED" in str(e):
                    reply = f"⚠️ Quota exceeded. Consider switching to another API key or check your plan.\n{e}"
                else:
                    reply = f"⚠️ Model request failed: {e}"

            st.markdown(reply)

    # Store assistant reply
    st.session_state.messages.append({"role": "assistant", "content": reply})

# -------------------- Footer --------------------
st.markdown("---")
st.markdown("<center>🚀 Built for IOAI practice with Streamlit + Gemini</center>", unsafe_allow_html=True)