import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FREELLMAPI_API_KEY"),
    base_url=os.getenv("FREELLMAPI_BASE_URL"),
)

response = client.chat.completions.create(
    model="auto",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI API gateway is in simple terms.",
        }
    ],
)

print("\n--- AI Response ---")
print(response.choices[0].message.content)

print("\n--- Routing ---")
print(f"Model: {response.model}")