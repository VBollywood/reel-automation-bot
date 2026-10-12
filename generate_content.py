import os
from datetime import datetime
from google import genai
from gtts import gTTS
from moviepy import AudioFileClip, ColorClip

api_key = os.environ.get("GEMINI_API_KEY")

def generate_ai_reel_script():
    if not api_key:
        print("Warning: GEMINI_API_KEY missing! Generating fallback script.")
        ai_script = "Hello dosto! Aaj hum baat karenge ek behad shandar AI tool ke baare mein jo aapke sabhi automation aur coding tasks ko kuch hi seconds mein poora kar sakta hai. Iske features aur istemal karne ke tareeqe ko hum step-by-step samjhenge taaki aapka kaam asan ho sake."
    else:
        try:
            client = genai.Client(api_key=api_key)
            # Bahut lambi aur detailed 30-40 second ki script ke liye prompt
            prompt = """
            Write a very long, high-energy, detailed 45-second Instagram Reel script in Hinglish about a powerful trending AI tool or software. 
            The script must contain:
            1. An engaging hook introducing the tool (0-10s).
            2. Detailed features and capabilities (10-30s).
            3. Step-by-step guide on how to use it (30-40s).
            4. A strong call to action to follow for more daily tech updates (40-45s).
            Write continuous natural speech paragraphs without any markdown, bullets, or brackets. Make sure the text is long enough to generate a full 30 to 40 seconds voiceover.
            """
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt,
            )
            ai_script = response.text
        except Exception as e:
            print(f"API Error: {str(e)}")
            ai_script = "Aaj ke is video mein hum explore kar rahe hain ek naya powerful AI software jo aapke sabhi automation tasks ko fast bana deta hai. Iske features aur use karne ke tareeqe ko hum step-by-step samjhenge taaki aap ise aasani se istemal kar sakein."

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    script_content = f"""========================================
AI TOOLS & SOFTWARE DEEP-DIVE - {current_time}
========================================

{ai_script}
"""

    # 1. Save Detailed Script
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    # 2. Generate Full Length Audio (Matched with long text)
    audio_path = "audio.mp3"
    try:
        tts = gTTS(text=ai_script, lang='hi', slow=False)
        tts.save(audio_path)
        print("Full length audio file generated successfully!")
    except Exception as e:
        print(f"Audio Generation Error: {str(e)}")
        return

    # 3. Video Rendering (Exact Audio Duration Match - No dead silence)
    try:
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration # Exact audio duration match hogi
        
        # Professional dark slate/indigo gradient background
        bg_clip = ColorClip(size=(720, 1280), color=(15, 23, 42)).with_duration(duration)
        video_clip = bg_clip.with_audio(audio_clip)
        
        video_output = "output_reel.mp4"
        video_clip.write_videofile(video_output, fps=24, codec="libx264", audio_codec="aac")
        print(f"Video reel generated successfully with exact duration: {duration} seconds!")
    except Exception as e:
        print(f"Video Generation Error: {str(e)}")

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    generate_ai_reel_script()
