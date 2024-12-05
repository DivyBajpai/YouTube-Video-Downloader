pip install streamlit-lottie
pip show streamlit-lottie
streamlit-lottie




import os
import subprocess
import time
import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url):
    """Fetch Lottie animation from URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def download_youtube_video_as_mp3(video_url, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        with st.spinner("Downloading and converting video..."):
            time.sleep(1)  # Simulate loading animation
            command = [
                "yt-dlp",
                "-x", "--audio-format", "mp3",  # Extract audio and convert to MP3
                "-o", os.path.join(output_directory, "%(title)s.%(ext)s"),  # Output format
                video_url
            ]
            subprocess.run(command, check=True)
            st.success("Video successfully downloaded and converted to MP3!")
    except subprocess.CalledProcessError as e:
        st.error(f"Failed to download or convert video: {video_url}. Error: {e}")

# Load animations
loading_animation = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_vfx6bktk.json")  # Replace with a suitable URL
success_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_ydo1amjm.json")  # Replace with a suitable URL

# Streamlit app
st.title("YouTube Video to MP3 Downloader")

st.markdown("### Built by Divy Bajpai")
st.markdown("#### Version: 1.0.1 Beta")

if loading_animation:
    st_lottie(loading_animation, height=200, key="loading")

video_url = st.text_input("Enter the YouTube video URL:")
output_directory = st.text_input("Enter the output directory for MP3 file:", "downloads")

if st.button("Download as MP3"):
    if video_url and output_directory:
        download_youtube_video_as_mp3(video_url, output_directory)
        if success_animation:
            st_lottie(success_animation, height=200, key="success")
    else:
        st.error("Please provide both the video URL and output directory.")
