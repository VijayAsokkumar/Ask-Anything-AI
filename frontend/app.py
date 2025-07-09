# frontend/app.py

import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agent.ai_agent import run_agent

st.set_page_config(page_title="Ask Anything Agent", layout="centered")
st.title("🧠 Ask Anything - AI Agent with Think / Reason / Act")

query = st.text_input("What do you want to ask the agent?")

if st.button("Run Agent") and query:
    with st.spinner("🧠 Thinking..."):
        result = run_agent(query)

        st.markdown("### 💭 Think")
        st.markdown(result["think"])

        st.markdown("### 🧩 Reason")
        st.markdown(result["reason"])

        st.markdown("### 🎯 Final Answer (Act)")
        st.success(result["act"])
