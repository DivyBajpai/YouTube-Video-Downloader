import os
import subprocess
import streamlit as st

def download_youtube_video_as_mp3(video_url, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        st.write(f"Downloading video: {video_url}")
        command = [
            "yt-dlp",
            "-x", "--audio-format", "mp3",  # Extract audio and convert to MP3
            "-o", os.path.join(output_directory, "%(title)s.%(ext)s"),  # Output format
            video_url
        ]
        subprocess.run(command, check=True)
        st.success(f"Video downloaded and converted to MP3 in {output_directory}")
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to download or convert video: {video_url}. Error: {e}")

# Streamlit app
st.title("YouTube Video to MP3 Downloader")

video_url = st.text_input("Enter the YouTube video URL:")
output_directory = st.text_input("Enter the output directory for MP3 file:", "downloads")

if st.button("Download as MP3"):
    if video_url and output_directory:
        download_youtube_video_as_mp3(video_url, output_directory)
    else:
        st.error("Please provide both the video URL and output directory.")
