"""
Basic Gemini call
"""

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # import APIKEY
    key = os.environ.get("GEMINI_KEY")
    # import client Gemini
    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="Explain how AI works",
    )

    print( type( response.text ) )
    
except NameError as e:
    print(f'O erro foi:\n{e}')
    