import google.generativeai as genai

# 🔑 Replace with your Gemini API key
genai.configure(api_key="AIzaSyDNhEJKSZLSXtzeBNLdQi4XGk39-Qe122w")

try:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content("Hello Gemini!")
    print("✅ Gemini API working!")
    print("Response:", response.text)
except Exception as e:
    print("❌ Error:", e)
