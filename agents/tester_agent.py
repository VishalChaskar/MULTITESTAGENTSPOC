import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_with_ai(page_data):
    prompt = f"""
You are a senior QA automation engineer.

Analyze this webpage:

Title: {page_data['title']}
Links: {page_data['links'][:10]}
Buttons: {page_data['buttons']}
Content: {page_data['text'][:1500]}

Return ONLY valid JSON:

{{
  "findings": [
    {{
      "category": "accessibility|navigation|content|usability",
      "severity": "critical|high|medium|low",
      "issue": "string",
      "suggestion": "string"
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Clean markdown if present
    if "```" in text:
        text = text.split("```")[1]

    return text