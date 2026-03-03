import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found from .env file.")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        # Add a user and assistant message for in-context learning
        messages=[
            {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
            {"role": "user", "content": "Give me a quick summary of Portugal."},
            {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
            {"role": "user", "content": "Give me a quick summary of Greece."}
        ]
    )
    return response.choices[0].message.content

get_response("")