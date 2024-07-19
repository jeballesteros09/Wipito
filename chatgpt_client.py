import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv("ks.env")

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

MODEL=""

def request_chat_gpt(user_message):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": user_message}
            ],temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""  
