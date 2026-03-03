import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found from .env file.")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    # Create a request to the Chat Completions endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=150,
        messages=[
            {"role":"system",
            "content": "You are a study planning assistant that creates plans for learning new skills."},
            {"role": "user",
            "content": "I want to learn to speak Dutch."}
        ]
    )
    # Extract the assistant's text response
    return response.choices[0].message.content

get_response("")