# How to Get Your OpenAI API Key

To use this chatbot, you need an OpenAI API key. Follow these steps:

1. Go to [https://platform.openai.com/signup](https://platform.openai.com/signup) and sign up (or log in if you already have an account).
2. Once logged in, go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).
3. Click on **"Create new secret key"** and copy the key.
4. **Never share your API key publicly.** Treat it like a password.

## Using the API Key

# === Option 1: Set the API key directly in your code (not recommended for production) ===

# Add this to your main Python file:
import openai
openai.api_key = "your-openai-api-key-here"

# === Option 2: Use environment variables (recommended) ===

# 1. Create a `.env` file in the root of your project directory.
# 2. Add your OpenAI API key like this (replace with your actual key):
# OPENAI_API_KEY=your-openai-api-key-here

# 3. Install the `python-dotenv` package if it's not already installed:
pip install python-dotenv

# 4. In your Python script (e.g., `app.py`), add this at the top:
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 5. Make sure your `.env` file is **not** pushed to GitHub.
# Add this line to your `.gitignore` file:
# .env
