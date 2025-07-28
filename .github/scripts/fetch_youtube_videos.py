#!/usr/bin/env python3
import os
import yaml
import json
from datetime import datetime
from googleapiclient.discovery import build

# YouTube channel ID for @faptured
CHANNEL_ID = 'UC' # You'll need to get your channel ID
API_KEY = os.environ.get('YOUTUBE_API_KEY')

def get_channel_id_from_username(youtube, username):
    """Get channel ID from username"""
    request = youtube.channels().list(
        part="id",
        forUsername=username
    )
    response = request.execute()
    
    if response['items']:
        return response['items'][0]['id']
    return None

def fetch_youtube_videos():
    """Fetch latest videos from YouTube channel"""
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Try to get channel ID from username first
    channel_id = get_channel_id_from_username(youtube, 'faptured')
    if not channel_id:
        channel_id = CHANNEL_ID
    
    # Get channel's uploads playlist
    channels_response = youtube.channels().list(
        id=channel_id,
        part='contentDetails'
    ).execute()
    
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    # Get videos from uploads playlist
    videos = []
    next_page_token = None
    
    while len(videos) < 50:  # Get up to 50 videos
        playlist_response = youtube.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()
        
        for item in playlist_response['items']:
            video_data = {
                'id': item['snippet']['resourceId']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'][:200] + '...' if len(item['snippet']['description']) > 200 else item['snippet']['description'],
                'thumbnail': item['snippet']['thumbnails'].get('maxres', item['snippet']['thumbnails']['high'])['url'],
                'publishedAt': item['snippet']['publishedAt'],
                'url': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
            }
            videos.append(video_data)
        
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return videos

def save_videos_data(videos):
    """Save videos data to Jekyll data file"""
    data_dir = '_data'
    os.makedirs(data_dir, exist_ok=True)
    
    # Save as YAML for Jekyll
    with open(os.path.join(data_dir, 'youtube_videos.yml'), 'w') as f:
        yaml.dump({
            'videos': videos,
            'last_updated': datetime.now().isoformat()
        }, f, default_flow_style=False)
    
    print(f"Saved {len(videos)} videos to _data/youtube_videos.yml")

def main():
    if not API_KEY:
        print("Error: YOUTUBE_API_KEY environment variable not set")
        return
    
    try:
        videos = fetch_youtube_videos()
        save_videos_data(videos)
    except Exception as e:
        print(f"Error fetching videos: {e}")

if __name__ == "__main__":
    main()