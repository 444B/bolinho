import streamlit as st
from openai import OpenAI
import os

client = OpenAI()

# Streamlit app title
st.title("OpenAI GPT-4o-mini Haiku Generator")

# Function to generate a haiku
def generate_haiku():
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming."
            }
        ]
    )
    return completion.choices[0].message

# Button to generate haiku
if st.button("Generate Haiku"):
    with st.spinner("Generating haiku..."):
        haiku = generate_haiku()
        st.write("### Haiku about Recursion in Programming")
        st.write(haiku)
