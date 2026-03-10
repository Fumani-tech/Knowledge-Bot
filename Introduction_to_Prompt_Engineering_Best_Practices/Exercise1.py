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
    # Define the conversation messages
    messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": "I am preparing event for my friend marriage"}
])
    return response.choices[0].message.content
response = get_response("")
print(response)