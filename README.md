# 🎥 Video Summarization Tool

## **📌 Overview**

The **Video Summarization Tool** is an AI-powered system that extracts, transcribes, and summarizes videos in real-time. It supports both **YouTube videos and local video files** using advanced **speech-to-text and natural language processing (NLP) techniques**.

This tool leverages **FFmpeg for audio extraction**, **OpenAI Whisper for speech recognition**, and **Google Gemini AI for summarization** to generate concise and meaningful summaries.

---

## **🛠️ Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/Video-Summarization-Tool.git
cd Video-Summarization-Tool
```

### **2️⃣ Create a Virtual Environment**

```bash
python -m venv venv_video_sum
source venv_video_sum/bin/activate  # For Mac/Linux
venv_video_sum\Scripts\activate     # For Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Install FFmpeg (If Not Installed)**

- **Mac/Linux:**
  ```bash
  brew install ffmpeg
  ```
- **Windows:**\
  Download and install from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

### **5️⃣ Add Your Google Gemini API Key**

- Get an API key from [Google AI Studio](https://ai.google.dev/)
- Set it as an environment variable:
  ```bash
  export GOOGLE_API_KEY="your_api_key_here"
  ```

---

## **🚀 How to Run the Application**

### **1️⃣ Start the Streamlit UI**

```bash
streamlit run app.py
```

- Upload a **local video** or **enter a YouTube link**.
- Click **Extract & Summarize** to generate a summary.

### **2️⃣ Run in CLI (Without UI)**

- Summarize a YouTube video:
  ```bash
  python extract_audio.py
  ```
- Summarize a local video:
  ```bash
  python extract_audio.py --file "data/sample.mp4"
  ```

---

## **📊 How It Works: Processing Pipeline**

```plaintext
  +------------------------+
  |  Video Source          |
  |  (YouTube/Local File)  |
  +------------------------+
            │
            ▼
  +---------------------------+
  |  Audio Extraction         |
  |  (FFmpeg - Convert Video  |
  |  to Audio)                |
  +---------------------------+
            │
            ▼
  +------------------------------+
  |  Speech-to-Text Conversion   |
  |  (Whisper / OpenAI ASR)      |
  |  Convert Audio → Text        |
  +------------------------------+
            │
            ▼
  +--------------------------------+
  |  Text Processing & Chunking   |
  |  (Splitting transcript        |
  |  into smaller sections)       |
  +--------------------------------+
            │
            ▼
  +---------------------------------+
  |  AI-Based Summarization        |
  |  (Google Gemini / OpenAI GPT)  |
  |  Generates Summary             |
  +---------------------------------+
            │
            ▼
  +------------------------+
  |  Final Summary Output  |
  |  (Text / JSON / UI)    |
  +------------------------+
```

---

## **🌟 Features of the Video Summarization Tool**

| Feature                                     | Description                                               |
| ------------------------------------------- | --------------------------------------------------------- |
| **Summarization of YouTube & Local Videos** | Process both online and offline videos                    |
| **Real-Time Processing**                    | No need to download full video; stream and summarize live |
| **Speech-to-Text Conversion**               | Uses Whisper to transcribe audio to text                  |
| **AI-Based Summarization**                  | Google Gemini / GPT creates meaningful summaries          |
| **Streamlit UI Support**                    | Easy-to-use web-based interface                           |
| **Multi-Format Support**                    | Works with MP4, AVI, MOV, and more                        |

---

## **🚀 Future Enhancements**

🔹 **Multi-Language Support** (Translate summaries)\
🔹 **Customizable Summarization Levels** (Short/Long summaries)\
🔹 **Real-Time Summarization with Faster Models**\
🔹 **Integration with Google Drive / Cloud Storage**

---

## **📌 Applications of This Tool**

✅ **Lecture Summarization** – Extract key points from recorded lectures.\
✅ **Podcast Summaries** – Quickly understand the main topics discussed.\
✅ **Meetings & Interviews** – Generate notes from meeting recordings.\
✅ **Content Creation** – Summarize long videos for social media.\
✅ **Educational Use** – Extract insights from tutorials and e-learning content.

---

## **📜 License**

This project is licensed under the **MIT License**.

---

## **👨‍💻 Author**

Developed by [Shalaka Padalkar](https://github.com/shalakapadalkar16).

---
