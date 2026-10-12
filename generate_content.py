import os
from datetime import datetime
from google import genai
from gtts import gTTS

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Warning: GEMINI_API_KEY missing! Generating fallback script.")
        ai_script = "Hello friends, welcome to our daily AI automation update."
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = "Create a short 15-second viral Hindi/Hinglish Instagram reel script about a cool tech tip. Keep it pure text without brackets or extra formatting so it sounds natural in audio."
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            ai_script = response.text
        except Exception as e:
            print(f"API Error: {str(e)}")
            ai_script = "Kya aapko pata hai AI se daily short videos auto-generate kiye ja sakte hain?"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
AI REEL SCRIPT - {current_time}
========================================

{ai_script}
"""

    # 1. Text script save karein
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    # 2. Text-to-Speech (Audio file create karein)
    try:
        tts = gTTS(text=ai_script, lang='hi', slow=False)
        tts.save("audio.mp3")
        print("Audio file (audio.mp3) generated successfully!")
    except Exception as e:
        print(f"Audio Generation Error: {str(e)}")

    print("Script and Voiceover process completed!")

if __name__ == "__main__":
    generate_ai_reel_script()
