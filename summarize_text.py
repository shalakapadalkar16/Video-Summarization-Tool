import google.generativeai as genai
import os

# Set your Google Gemini API key
GEMINI_API_KEY = "AIzaSyDwol6WJfX4nxUjujzDM-vWOY4ILuRWHn8"  # Replace with your actual API key

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def summarize_text(text):
    """Summarizes the given transcript using Google Gemini AI."""
    print("⏳ Generating summary with Google Gemini...")

    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")  # Use an available model

    response = model.generate_content(f"Summarize this transcript:\n{text}")

    summary = response.text  # Extract generated summary
    print("✅ Summary generated successfully!")
    return summary

# Example Usage
if __name__ == "__main__":
    with open("audio/transcription.txt", "r") as f:
        transcript = f.read()
    
    summary = summarize_text(transcript)
    print("\n📄 Summary:\n", summary)

    with open("audio/summary.txt", "w") as f:
        f.write(summary)