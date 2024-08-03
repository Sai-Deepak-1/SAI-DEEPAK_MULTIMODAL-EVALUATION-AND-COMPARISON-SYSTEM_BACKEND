import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Multimodal Evaluation and Comparison System")

task = st.selectbox("Select Task", ["text-classification", "ner", "question-answering", "summarization"])
text_input = st.text_area("Enter Text")

if st.button("Evaluate"):
    if text_input:
        response = requests.post(f"{API_URL}/evaluate/", json={"text": text_input, "task": task})
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Error: " + response.text)
    else:
        st.error("Please enter text to evaluate.")

if st.button("Check Health"):
    response = requests.get(f"{API_URL}/health/")
    if response.status_code == 200:
        st.success("Service is healthy!")
    else:
        st.error("Service is not healthy!")
