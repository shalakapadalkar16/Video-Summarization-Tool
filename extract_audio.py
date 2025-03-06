import moviepy.editor as mp
import os

# Ensure MoviePy uses the correct FFMPEG path
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"  # Update with correct path

def extract_audio(video_path, audio_path):
    """Extracts audio from a given video file and saves it."""

    # Ensure output directory exists
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    try:
        video = mp.VideoFileClip(video_path)
        
        if not video.audio:
            raise ValueError("No audio found in the video file!")

        video.audio.write_audiofile(audio_path)
        print(f"✅ Audio extracted successfully: {audio_path}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{video_path}' was not found.")
    except Exception as e:
        print(f"❌ An error occurred: {str(e)}")

# Example Usage
if __name__ == "__main__":
    extract_audio("data/input.mp4", "audio/extracted_audio.wav")