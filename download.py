import os
import subprocess
from yt_dlp import YoutubeDL

# Set input and output directories
input_directory = "./videos"
output_directory = "./compressed_videos"

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download videos using yt_dlp
ydl_opts = {
    'format': 'bestvideo[height<=480]+bestaudio/best',
    'outtmpl': os.path.join(input_directory, '%(id)s.%(ext)s'),
}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([input("Video/Playlist/Channel URL: ")])

# Compress downloaded videos to 480p resolution, 30fps frame rate, and 128k audio bitrate
for filename in os.listdir(input_directory):
    input_file = os.path.join(input_directory, filename)
    if os.path.isfile(input_file):
        filename_without_extension, extension = os.path.splitext(filename)
        output_file = os.path.join(output_directory, f"{filename_without_extension}_480p_compressed.mp4")
        subprocess.run([
            'ffmpeg',
            '-i', input_file,
            '-vf', 'scale=-1:360',
            '-r', '30',
            '-c:v', 'libx264',
            '-crf', '23',
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '64k',
            output_file
        ], capture_output=True)  # Capture output to suppress unnecessary output