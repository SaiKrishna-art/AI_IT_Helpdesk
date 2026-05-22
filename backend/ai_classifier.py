import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_ticket(ticket_text):
    prompt = f"""
You are an IT helpdesk AI assistant.
Analyze the IT support issue below and return ONLY a valid JSON object. 
No explanation. No markdown. No extra text. Just the JSON.

Required fields:
- category (one of: Network, Hardware, Security, Software)
- priority (one of: Low, Medium, High, Critical)
- assignment_group (one of: Network Team, Hardware Team, Security Team, Software Team, IT Support)
- solution (a short suggested fix, 1-2 sentences)

Issue:
{ticket_text}
"""
    response = model.generate_content(prompt)
    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    return json.loads(text)