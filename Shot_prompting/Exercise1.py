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
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

response = get_response("""Classify the sentiment of each review from 1 to 5.:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable. 
4. Can't wait to show them off!""")
print(response)