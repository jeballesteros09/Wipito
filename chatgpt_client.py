import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv("ks.env")

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def request_chat_gpt(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ],temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""  
