import os
import google.generativeai as genai
from datetime import datetime

# API Key configure karein jo GitHub Secrets se aayegi
api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Error: GEMINI_API_KEY not found!")
        return

    genai.configure(api_key=api_key)
    
    # Gemini model select karein
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """
    Create a short, viral YouTube/Instagram reel script in Hinglish about an interesting tech, AI, or productivity fact. 
    Format it strictly into:
    1. HOOK (0-3 seconds)
    2. BODY CONTENT (3-20 seconds)
    3. CALL TO ACTION (20-30 seconds)
    Keep it punchy and engaging.
    """

    try:
        response = model.generate_content(prompt)
        ai_script = response.text
    except Exception as e:
        ai_script = f"Error generating script via AI: {str(e)}"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
AI GENERATED REEL SCRIPT - {current_time}
========================================

{ai_script}
"""

    # 'reel_script.txt' file mein save karein
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("AI-powered Reel Script successfully generated!")

if __name__ == "__main__":
    generate_ai_reel_script()
