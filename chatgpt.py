"""
Basic OpenAI call
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # import OpenAI Key 
    api_key = os.getenv('OPENAI_KEY')
    # construct OpenAI client instance
    client = OpenAI(
        api_key=api_key
    )
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "Write a one-sentence bedtime story about a unicorn."
            }
        ]
    )
    print(completion.choices[0].message.content)
    
except NameError as e:
    print(f'O erro foi:\n{e}')
    