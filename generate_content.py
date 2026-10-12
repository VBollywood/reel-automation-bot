import os
from datetime import datetime
from google import genai
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Warning: GEMINI_API_KEY missing! Generating fallback script.")
        ai_script = "Hello dosto, aaj hum baat karenge duniya ke sabse behtareen AI tools aur software ke baare mein jo aapke kaam ko asan kar sakte hain. Is video mein hum dekhenge ki kaise alag-alag apps features aur step-by-step use kiye jate hain."
    else:
        try:
            client = genai.Client(api_key=api_key)
            # Strict prompt taaki lambi aur detail script bane
            prompt = """
            Write a detailed, high-energy 30-to-40 seconds Instagram Reel script in Hinglish about a trending AI tool, software, or GitHub automation app. 
            Do not make it short. Include:
            1. Introduction of the tool and what problem it solves.
            2. Detailed features and step-by-step usage guide.
            3. Why developers or creators should use it.
            4. Clear Call to Action at the end.
            Keep the language natural, conversational, and engaging for audio voiceover. No brackets or markdown symbols.
            """
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            ai_script = response.text
        except Exception as e:
            print(f"API Error: {str(e)}")
            ai_script = "Aaj ke is video mein hum explore kar rahe hain ek naya powerful AI software jo aapke sabhi automation tasks ko automate kar sakta hai. Iske features aur use karne ke tareeqe ko hum step-by-step samjhenge."

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
AI TOOLS & SOFTWARE DEEP-DIVE - {current_time}
========================================

{ai_script}
"""

    # 1. Save Script
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    # 2. Generate Audio (Longer text will result in 30-40s audio)
    audio_path = "audio.mp3"
    try:
        tts = gTTS(text=ai_script, lang='hi', slow=False)
        tts.save(audio_path)
        print("Extended audio file generated successfully!")
    except Exception as e:
        print(f"Audio Generation Error: {str(e)}")
        return

    # 3. Video Rendering (Ensuring minimum 30 seconds or matching audio length)
    try:
        audio_clip = AudioFileClip(audio_path)
        duration = max(audio_clip.duration, 30.0) # Ensure at least 30 seconds duration
        
        # Professional dark blue/indigo gradient background look
        bg_clip = ColorClip(size=(720, 1280), color=(30, 41, 59)).with_duration(duration)
        video_clip = bg_clip.with_audio(audio_clip)
        
        video_output = "output_reel.mp4"
        video_clip.write_videofile(video_output, fps=24, codec="libx264", audio_codec="aac")
        print("30+ seconds video reel generated successfully!")
    except Exception as e:
        print(f"Video Generation Error: {str(e)}")

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
