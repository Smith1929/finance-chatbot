import streamlit as st
import google.generativeai as genai
from datetime import datetime

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="💬 Finance Chatbot", page_icon="💰", layout="centered")

# ------------------------------
# Configure Gemini API
# ------------------------------
genai.configure(api_key=st.secrets["general"]["GEMINI_API_KEY"])

# ------------------------------
# Custom CSS (WhatsApp-like UI)
# ------------------------------
st.markdown("""
    <style>
    body {
        background-color: #e5ddd5;
    }
    .chat-container {
        max-width: 600px;
        margin: auto;
        background-color: #ffffff;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
    }
    .user-msg {
        background-color: #2e2d2a;
        color: #ffffff;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        text-align: right;
        float: right;
        clear: both;
        max-width: 75%;
    }
    .bot-msg {
        background-color: #2e2d2a;
        color: #ffffff;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        text-align: left;
        float: left;
        clear: both;
        max-width: 75%;
    }
    .timestamp {
        font-size: 10px;
        color: gray;
        text-align: right;
        margin-top: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# Initialize Session State
# ------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------------
# Header
# ------------------------------
st.markdown("<h2 style='text-align:center;'>💬 Finance Chatbot</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Ask anything about finance, investments, or economics.</p>", unsafe_allow_html=True)

# ------------------------------
# Chat Container
# ------------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>{msg['content']}<div class='timestamp'>{msg['time']}</div></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{msg['content']}<div class='timestamp'>{msg['time']}</div></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# User Input
# ------------------------------
user_input = st.chat_input("Type your message...")

# ------------------------------
# On Send
# ------------------------------
if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": datetime.now().strftime("%H:%M")
    })

    # Get Gemini response
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(user_input)

    # Add bot message
    st.session_state.messages.append({
        "role": "bot",
        "content": response.text,
        "time": datetime.now().strftime("%H:%M")
    })

    # Rerun to show new message
    st.rerun()
