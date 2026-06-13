import google.generativeai as genai

genai.configure(api_key="API")

model = genai.GenerativeModel("gemini-3.5-flash")

response = model.generate_content("Как тебя зовут?") #text
print(response.text)