import google.generativeai as genai

# Replace with your API key
genai.configure(api_key="AIzaSyDNhEJKSZLSXtzeBNLdQi4XGk39-Qe122w")

models = genai.list_models()
for m in models:
    print(m.name)
