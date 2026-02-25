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
        temperature=2,
        messages=[{"role": "user", "content": prompt}]
        
    )
    return response.choices[0].message.content

response = get_response("""
I need a product description for SonicPro headphones, wireless headphone with 40 hour of battery life. Active noise cancellation (ANC), foldable design
""")
print(response)