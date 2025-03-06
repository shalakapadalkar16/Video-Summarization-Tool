import whisper

def transcribe_audio(audio_path):
    """Transcribes audio to text using OpenAI Whisper."""
    print("⏳ Transcribing audio, this may take a few moments...")
    
    # Load Whisper model (choose from: tiny, base, small, medium, large)
    model = whisper.load_model("base")

    # Transcribe audio
    result = model.transcribe(audio_path)

    print("✅ Transcription completed successfully!")
    return result["text"]

# Example Usage:
if __name__ == "__main__":
    transcript = transcribe_audio("audio/extracted_audio.wav")
    print("\n🎤 Transcription:\n", transcript)

    # Save the transcript to a file
    with open("audio/transcription.txt", "w") as f:
        f.write(transcript)