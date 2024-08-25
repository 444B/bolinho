
### Setup Instructions

1. **Check Python Version**  
   ```bash
   python3 --version
   ```

2. **Set Up Virtual Environment**  
   ```bash
   pipenv --python 3.12
   pipenv shell
   ```

3. **Install Dependencies**  
   ```bash
   pipenv sync
   ```

4. **Set OPENAI API Key**

   - On MacOS/Linux:  
     ```bash
     export OPENAI_API_KEY="your-openai-api-key"
     ```

   - On Windows:  
     ```bash
     set OPENAI_API_KEY="your-openai-api-key"
     ```

5. **Run the Application**  
   ```bash
   streamlit run app.py
   ```

6. *(Optional)* **Test Streamlit Installation**  
   ```bash
   streamlit hello
   ```
