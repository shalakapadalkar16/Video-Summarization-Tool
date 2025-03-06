import streamlit as st
import os
from extract_audio import extract_audio, download_youtube_video  # Now uses yt-dlp
from transcribe_audio import transcribe_audio
from summarize_text import summarize_text

# Set page title
st.set_page_config(page_title="🎥 Video Summarizer", layout="wide")

st.title("🎥 AI-Powered Video Summarization")
st.write("Upload a video file or enter a YouTube link to get a concise AI-generated summary.")

# Input for YouTube link
youtube_url = st.text_input("Enter YouTube URL (or upload a file)")

# File uploader for local videos
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

video_path = None

if youtube_url:
    st.write("📥 Downloading YouTube video...")
    video_path = download_youtube_video(youtube_url)  # Now uses yt-dlp
    if video_path:
        st.video(video_path)  # Show downloaded video
    else:
        st.error("❌ Failed to download the video. Please check the link or try another.")

elif uploaded_file:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    video_path = "uploaded_video.mp4"
    st.video(video_path)

if video_path:
    if st.button("📢 Extract & Summarize"):
        st.write("⏳ Extracting audio...")
        
        # Extract audio
        extract_audio(video_path, "audio/extracted_audio.wav")
        st.success("🎵 Audio extracted successfully!")

        # Transcribe audio
        st.write("⏳ Transcribing audio...")
        transcription = transcribe_audio("audio/extracted_audio.wav")
        st.text_area("📝 Transcript", transcription, height=200)

        # Summarize transcript
        st.write("⏳ Generating summary...")
        summary = summarize_text(transcription)
        st.subheader("📃 AI-Generated Summary")
        st.write(summary)

        # Save summary
        with open("audio/summary.txt", "w") as f:
            f.write(summary)
        
        st.success("✅ Summary saved!")