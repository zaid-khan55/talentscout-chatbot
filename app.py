import streamlit as st
from openai import OpenAI
from prompts import SYSTEM_PROMPT, TECH_QUESTION_PROMPT
from utils import is_exit_message

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------------- OpenAI Client ----------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------------- Session State Init ----------------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.messages = []
    st.session_state.input_buffer = ""

# ---------------- Constants ----------------
FIELDS = [
    "Full Name",
    "Email Address",
    "Phone Number",
    "Years of Experience",
    "Desired Position(s)",
    "Current Location",
    "Tech Stack (comma-separated)"
]

# ---------------- Message Handler ----------------
def handle_input():
    user_input = st.session_state.input_buffer.strip()
    if not user_input:
        return

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Exit handling
    if is_exit_message(user_input):
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                "Thank you for your time! "
                "Our recruitment team will contact you if your profile matches."
            )
        })
        st.session_state.input_buffer = ""
        return

    # Information collection
    if st.session_state.step < len(FIELDS):
        field = FIELDS[st.session_state.step]
        st.session_state.data[field] = user_input
        st.session_state.step += 1

        if st.session_state.step < len(FIELDS):
            reply = f"Please enter your **{FIELDS[st.session_state.step]}**."
        else:
            reply = "Thank you! I’m generating technical questions for you..."

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )

    # Technical question generation
    else:
        tech_stack = st.session_state.data["Tech Stack (comma-separated)"]
        prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": "You may type **exit** to end the conversation."
        })

    # Clear input SAFELY
    st.session_state.input_buffer = ""

# ---------------- UI ----------------
st.title("🤖 TalentScout – AI Hiring Assistant")
st.write(
    "Welcome! I’ll guide you through an initial technical screening. "
    "Type **exit** anytime to end the conversation."
)

# ---------------- Chat History ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- Input Box ----------------
st.text_input(
    "You:",
    placeholder="Type your response and press Enter",
    key="input_buffer",
    on_change=handle_input
)
