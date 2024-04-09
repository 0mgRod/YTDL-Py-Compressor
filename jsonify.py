from pytube import YouTube 
import os
import base64
import json

# Function to get video details using pytube
def get_video_details(video_url):
    yt = YouTube(video_url)
    return {
        "video_name": yt.title,
        "total_views": yt.views,
        "creator": yt.author,
        "thumbnail_url": yt.thumbnail_url
    }

# Function to generate base64 thumbnail image
def get_thumbnail_base64(thumbnail_url):
    import requests
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        thumbnail_data = response.content
        return base64.b64encode(thumbnail_data).decode('utf-8')
    else:
        return None

# Path to videos folder
videos_folder = "./videos"
# Path to data folder
data_folder = "./data"

# Create data folder if it does not exist
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

# Iterate over files in the videos folder
for filename in os.listdir(videos_folder):
    video_id, extension = os.path.splitext(filename)
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_details = get_video_details(video_url)
    
    if video_details:
        # Generating base64 encoded thumbnail
        thumbnail_base64 = get_thumbnail_base64(video_details['thumbnail_url'])
        
        # Creating a dictionary with video details
        video_info = {
            "video_name": video_details['video_name'],
            "total_views": video_details['total_views'],
            "creator": video_details['creator'],
            "thumbnail_base64": thumbnail_base64
        }
        
        # Write video details to JSON file
        with open(f"{data_folder}/{video_id}.json", "w") as json_file:
            json.dump(video_info, json_file)

print("JSON files generated successfully in the data folder!")