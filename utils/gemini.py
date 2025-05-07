import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API Key
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env file")

# Configure Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

async def call_gemini_api(prompt: str):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(
            prompt
        )
        return response.text  # Return only the generated text
    except Exception as e:
        return {"error": str(e)}