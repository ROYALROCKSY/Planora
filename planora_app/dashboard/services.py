# dashboard/services.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ["GENAI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Initialize GenAI client
client = genai.Client()

async def call_gemini_api(prompt: str) -> str:
    """
    Call Gemini 2.5 Flash via official client and return the bot response.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        
        )
        return response.text
    except Exception as e:
        return f"(Gemini API error: {e})"
