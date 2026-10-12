import os
from datetime import datetime
from google import genai
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Warning: GEMINI_API_KEY missing! Generating fallback script.")
        ai_script = "Hello dosto, aaj hum seekhenge ek naye AI tool ke baare mein jo aapka kaam asan kar dega."
    else:
        try:
            client = genai.Client(api_key=api_key)
            # Universal AI prompt jo kisi bhi naye AI tool, app, software ya GitHub tool ko uthayega
            prompt = """
            Aap ek expert AI tech creator hain jo Instagram Reels aur YouTube Shorts ke liye script likhte hain.
            Internet par maujood kisi bhi ek behtareen AI tool, software, application ya developer tool (jaise ChatGPT, Claude, Cursor, Midjourney, v0, GitHub Copilot, ElevenLabs, etc. ya koi bhi naya trending AI tool) ko randomly chuniye jo repeat na ho.
            
            Us tool par ek 30-second ki engaging Hinglish script banaiye jismein yeh shamil ho:
            1. Hook (0-5s): Tool ka naam aur uska sabse bada fayda.
            2. Features & Use Case (5-20s): Yeh kya karta hai aur ise step-by-step kaise istemal karein.
            3. Call to Action (20-30s): Follow for more daily AI tools updates.
            
            Script bilkul natural, clear aur conversational honi chahiye bina kisi extra brackets ke taaki voiceover mein acchi lage.
            """
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            ai_script = response.text
        except Exception as e:
            print(f"API Error: {str(e)}")
            ai_script = "Aaj ke is video mein hum baat karenge ek naye AI automation tool ki jo aapke sabhi tasks ko fast bana deta hai."

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
DAILY AI & GITHUB TOOLS REEL SCRIPT - {current_time}
========================================

{ai_script}
"""

    # 1. Detailed Script Save Karein
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    # 2. Text-to-Speech (Longer Voice-over for 30 seconds)
    audio_path = "audio.mp3"
    try:
        tts = gTTS(text=ai_script, lang='hi', slow=False)
        tts.save(audio_path)
        print("Detailed audio file generated successfully!")
    except Exception as e:
        print(f"Audio Generation Error: {str(e)}")
        return

    # 3. Video Rendering with Audio Duration (Longer duration support)
    try:
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration
        
        # Background video/color matching the audio duration
        bg_clip = ColorClip(size=(720, 1280), color=(15, 23, 42)).with_duration(duration)
        video_clip = bg_clip.with_audio(audio_clip)
        
        video_output = "output_reel.mp4"
        video_clip.write_videofile(video_output, fps=24, codec="libx264", audio_codec="aac")
        print("Complete 30-second AI Tool video reel generated successfully!")
    except Exception as e:
        print(f"Video Generation Error: {str(e)}")

    print("Automation pipeline finished successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
