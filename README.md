### Run this for setup

python3 --version
pipenv --python 3.12
pipenv install streamlit
pipenv shell

(On MacOS/Linux)
export OPENAI_API_KEY="your-openai-api-key"

(On Windows)
set OPENAI_API_KEY="your-openai-api-key"

streamlit run app.py
(optionally - streamlit hello)