import streamlit as st
import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is available
if not openai.api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()

# Streamlit app title
st.title("OpenAI API Demonstration")

# Sidebar for navigation
st.sidebar.title("Select a Demo")
demo_option = st.sidebar.selectbox("Choose a capability:", 
                                   ["Text Generation", "Text Summarization", "Sentiment Analysis", "Code Generation"])

# Function to call OpenAI API
def call_openai(prompt, max_tokens=100, temperature=0.7, stop=None, model="text-davinci-003"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        stop=stop
    )
    return response.choices[0].text.strip()

# Text Generation Demo
if demo_option == "Text Generation":
    st.header("Text Generation")
    user_input = st.text_area("Enter a prompt:", "Once upon a time")
    if st.button("Generate"):
        with st.spinner("Generating text..."):
            generated_text = call_openai(user_input)
            st.write("Generated Text:")
            st.write(generated_text)

# Text Summarization Demo
elif demo_option == "Text Summarization":
    st.header("Text Summarization")
    user_input = st.text_area("Enter text to summarize:", "OpenAI's GPT-4 is a powerful language model...")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary_prompt = f"Summarize the following text:\n\n{user_input}\n\nSummary:"
            summary = call_openai(summary_prompt, max_tokens=50)
            st.write("Summary:")
            st.write(summary)

# Sentiment Analysis Demo
elif demo_option == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    user_input = st.text_area("Enter text to analyze sentiment:", "I love using Streamlit with OpenAI!")
    if st.button("Analyze Sentiment"):
        with st.spinner("Analyzing sentiment..."):
            sentiment_prompt = f"Analyze the sentiment of the following text:\n\n{user_input}\n\nSentiment:"
            sentiment = call_openai(sentiment_prompt, max_tokens=10, temperature=0)
            st.write("Sentiment:")
            st.write(sentiment)

# Code Generation Demo
elif demo_option == "Code Generation":
    st.header("Code Generation")
    user_input = st.text_area("Enter a code description or prompt:", "Write a Python function to calculate the factorial of a number.")
    if st.button("Generate Code"):
        with st.spinner("Generating code..."):
            code_prompt = f"Generate Python code for the following task:\n\n{user_input}\n\nPython Code:"
            code = call_openai(code_prompt, max_tokens=150, stop=["#"])
            st.code(code, language='python')
