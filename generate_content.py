import os
import google.generativeai as genai
from datetime import datetime

# API Key check karein
api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Error: GEMINI_API_KEY is missing!")
        ai_script = "Default Script: AI Automation is future."
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = "Create a short viral Hinglish Instagram reel script about AI in 3 parts: Hook, Body, Call to Action."
            response = model.generate_content(prompt)
            ai_script = response.text
        except Exception as e:
            ai_script = f"Error during generation: {str(e)}"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
AI REEL SCRIPT - {current_time}
========================================

{ai_script}
"""

    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("Script updated successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
