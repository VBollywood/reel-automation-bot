import os
from datetime import datetime
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Error: GEMINI_API_KEY missing!")
        ai_script = "Default Script: AI Automation is the future."
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = "Create a short, viral Hinglish Instagram reel script about AI in 3 parts: Hook (0-3s), Body (3-20s), Call to Action (20-30s)."
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
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
    
    print("Script generated successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
