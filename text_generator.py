import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_natural_english(text):
    return _generate_text(text, "Make this natural English:")

def generate_emoji(text):
    return _generate_text(text, "Convert this text to a single emoji:")

def _generate_text(text, instruction):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{instruction} {text}"},
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].message.content