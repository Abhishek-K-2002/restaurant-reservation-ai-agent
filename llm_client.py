import google.generativeai as genai
import traceback
import re
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('Gemini_API'))

def call_llm_api(user_input):
    try:
        prompt = f"""
You are an AI assistant for a restaurant reservation system.
Classify the user's intent strictly as one of the following:
["recommend_restaurant", "book_table","greeting", "fallback"].
Return a JSON with key 'intent' only.

User: "{user_input}"

Example response:
{{
  "intent": "recommend_restaurant"
}}
"""
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(temperature=0.2)
        )

        if response and hasattr(response, 'text'):
            raw_output = response.text.strip()
            # Remove backticks, language hints etc.
            cleaned_output = re.sub(r'^```(json)?\s*|```$', '', raw_output, flags=re.IGNORECASE).strip()
            return cleaned_output
        else:
            return '{"intent": "fallback"}'

    except Exception as e:
        traceback.print_exc()
        return '{"intent": "fallback"}'