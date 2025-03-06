import moviepy.editor as mp
import os
import subprocess
from pytube import YouTube

# Ensure MoviePy uses the correct FFMPEG path
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"  # Update if needed

def download_youtube_video(youtube_url, output_path="downloaded_video.mp4"):
    """Downloads a YouTube video using yt-dlp and saves it as an MP4 file."""
    try:
        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",  # Select best quality
            "-o", output_path,
            youtube_url
        ]
        subprocess.run(command, check=True)
        print(f"✅ YouTube video downloaded successfully: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error downloading YouTube video: {e}")
        return None

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
    youtube_url = input("Enter YouTube Video URL: ")  # Ask for YouTube link
    video_path = download_youtube_video(youtube_url)
    
    if video_path:
        extract_audio(video_path, "audio/extracted_audio.wav")