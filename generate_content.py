import os
from datetime import datetime
from google import genai
from gtts import gTTS
from moviepy.editor import AudioFileClip, ColorClip

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Warning: GEMINI_API_KEY missing! Generating fallback script.")
        ai_script = "Hello friends, welcome to our daily AI automation update."
    else:
        try:
            client = genai.Client(api_key=api_key)
            prompt = "Create a short 15-second viral Hindi/Hinglish Instagram reel script about a cool tech tip. Keep it pure text without brackets."
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
    audio_path = "audio.mp3"
    try:
        tts = gTTS(text=ai_script, lang='hi', slow=False)
        tts.save(audio_path)
        print("Audio file generated successfully!")
    except Exception as e:
        print(f"Audio Generation Error: {str(e)}")
        return

    # 3. Video Rendering (MoviePy se MP4 video banayein)
    try:
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration
        
        # Vertical reel size (720x1280) aur dark background color set karein
        bg_clip = ColorClip(size=(720, 1280), color=(20, 20, 40), duration=duration)
        
        # Audio ko video ke sath combine karein
        video_clip = bg_clip.set_audio(audio_clip)
        
        # Final video output save karein
        video_output = "output_reel.mp4"
        video_clip.write_videofile(video_output, fps=24, codec="libx264", audio_codec="aac")
        print("Video reel (output_reel.mp4) generated successfully!")
    except Exception as e:
        print(f"Video Generation Error: {str(e)}")

    print("Complete Reel Pipeline finished successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
