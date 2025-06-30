import os 
import sys
import openai
import httpx
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


load_dotenv()

# Load secure values from .env
API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL_ID = os.getenv("MODEL_ID")

def ask_llm_via_openrouter(query):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "HTTP-Referer": "http://localhost",  # Use your domain if deploying
            "X-Title": "SmartStudentCLI"
        }

        payload = {
            "model": MODEL_ID,
            "messages": [
                {"role": "user", "content": query}
            ]
        }

        response = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Error: {str(e)}"
