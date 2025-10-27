import streamlit as st
import os
import json
from agent.graph import agent

generated_dir = "generated_project"

# Session memory for prompts and results
if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("Coder Buddy: AI Code Generator")

# Sidebar: List generated projects
st.sidebar.header("Generated Projects")
projects = []
if os.path.exists(generated_dir):
    for root, dirs, files in os.walk(generated_dir):
        for d in dirs:
            projects.append(d)
        break  # Only top-level dirs
if projects:
    st.sidebar.write("\n".join(projects))
else:
    st.sidebar.write("No projects yet.")

# Main input box
user_prompt = st.text_input("Enter your project prompt:", "")
if st.button("Generate Project") and user_prompt:
    with st.spinner("Generating project..."):
        result = agent.invoke({"user_prompt": user_prompt}, {"recursion_limit": 100})
        st.session_state["history"].append({"prompt": user_prompt, "result": result})
        st.success("Project generated!")
        st.write("Final State:", result)

# Show session memory
st.header("Session History")
for item in st.session_state["history"]:
    st.markdown(f"**Prompt:** {item['prompt']}")
    st.json(item["result"])
