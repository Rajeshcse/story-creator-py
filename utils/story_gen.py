import os
import google.generativeai as genai # type: ignore
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_story(prompt, age_group, pages):
    instructions = (
        f"You are a children's story writer. Create a magical story for children aged {age_group} "
        f"based on the idea: '{prompt}'. Break it into {pages} short, simple chapters with titles. "
        f"Use a warm, friendly tone suitable for young readers."
    )

    # ✅ Use content in a list for the new v1 method
    response = model.generate_content([instructions])

    return response.text
