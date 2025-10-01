# planora_app/flashcards/flashcards_services.py
from google import genai
import os
from dotenv import load_dotenv
import re

load_dotenv()
os.environ["GENAI_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Initialize client once
client = genai.Client()

def generate_flashcards(user_id: str, text: str) -> list:
    """
    Calls Gemini API to summarize text into 5-10 concise flashcards.
    Returns a list of dictionaries with 'text' for each flashcard.
    """
    prompt = (
        "Summarize the following text into 5–10 extremely concise flashcards.\n"
        "Each flashcard must be short (around 20-25 words) and focus only on key points.\n"
        "Do not include preambles like 'Here are x flashcards' or numbering.\n"
        "Do not include markdown symbols like * or **.\n\n"
        f"Text:\n{text}"
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        raw_text = response.text

        # Split into lines and clean
        lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
        flashcards = []

        for line in lines:
            # Remove markdown symbols and leading bullets/numbers
            clean_line = re.sub(r'^[\*\-\d\.\s]+', '', line)
            clean_line = clean_line.replace('**', '').strip()
            # Skip lines like "Here are x flashcards..."
            if clean_line.lower().startswith("here are"):
                continue
            if clean_line:
                flashcards.append({"text": clean_line})

        # Ensure max 10 flashcards
        flashcards = flashcards[:10]

        # Fallback if Gemini returns nothing
        if not flashcards:
            flashcards = [{"text": "Error generating flashcards"}]

        return flashcards

    except Exception as e:
        print(f"[Flashcards Service Error] {e}")
        return [{"text": "Error generating flashcards"}]
