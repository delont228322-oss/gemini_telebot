from google import genai
from google.genai import types
client = genai.Client (api_key="API")

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="", #promt
        config=types.GenerateContentConfig(
            system_instruction="", #text
            temperature=0.8,
            max_output_tokens=800 #so many words
        )
    )
    print(response.text)
except Exception as e:
    print(f"Ошибка: {e}") #error operation
