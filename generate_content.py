import os

def create_reel_script():
    topic = "AI Tools for Productivity"
    
    script_content = f"""
    Topic: {topic}
    - Hook (0-3 sec): Kya aapko pata hai AI kaise aapka aadha kaam kam kar sakta hai?
    - Body (3-20 sec): Yeh rahe top 3 tools jo aapke daily task automate kar denge.
    - Call to Action (20-30 sec): Maze ki reels ke liye follow karein!
    """
    
    with open("reel_script.txt", "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("Reel script successfully generated!")

if __name__ == "__main__":
    create_reel_script()
