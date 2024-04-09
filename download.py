import os
import subprocess
from yt_dlp import YoutubeDL

# Set input and output directories
input_directory = "./videos"

# Create output directory if it doesn't exist
os.makedirs(input_directory, exist_ok=True)

# Download videos using yt_dlp
ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio/best',
    'outtmpl': os.path.join(input_directory, '%(id)s.%(ext)s'),
}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([input("Video/Playlist/Channel URL: ")])