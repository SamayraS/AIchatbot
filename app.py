from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate

# Load the API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.title("Story Generator with Gemini")
st.divider()
topic = st.text_input("Enter a topic for your story")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short story about {topic}."
)

st.divider()
if topic:
    full_prompt = prompt.format(topic=topic)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(full_prompt)
    st.write(response.text)
