import streamlit as st
from openai import OpenAI
import os

client = OpenAI()

# Streamlit app title
st.markdown("# ⚠️OpenAI GPT testing area⚠️")

# Function to run the prompt
def run_prompt(user_code):
    # Execute the user code in a controlled environment
    # WARNING: This approach runs arbitrary code and should be used with caution.
    # For a safer alternative, avoid eval/exec and consider another method to process the input.
    local_vars = {}
    exec(user_code, {"client": client, "OpenAI": OpenAI}, local_vars)
    return local_vars

# Input box for user to enter their code
user_code = st.text_area("Enter your code here:")

# Button to generate the response
if st.button("Do it!"): 
    with st.spinner("tHinKiNG weLLy haWD! one sec UwU 🧠💨"):
        try:
            response = run_prompt(user_code)
            st.markdown("## --- Response ---")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
