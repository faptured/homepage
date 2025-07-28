#!/usr/bin/env python3
import os
import yaml
import feedparser
import requests
from datetime import datetime
from urllib.parse import parse_qs, urlparse

# YouTube channel URLs to try
CHANNEL_URLS = [
    'https://www.youtube.com/@faptured',
    'https://www.youtube.com/c/faptured',
    'https://www.youtube.com/user/faptured'
]

def get_channel_id():
    """Try to get channel ID from YouTube channel page"""
    for url in CHANNEL_URLS:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                # Look for channel ID in the response
                content = response.text
                
                # Method 1: Look for channelId in the page
                if '"channelId":"' in content:
                    start = content.find('"channelId":"') + 14
                    end = content.find('"', start)
                    channel_id = content[start:end]
                    if channel_id.startswith('UC'):
                        print(f"Found channel ID: {channel_id}")
                        return channel_id
                
                # Method 2: Look for channel URL
                if 'youtube.com/channel/' in content:
                    start = content.find('youtube.com/channel/') + 20
                    end = content.find('"', start)
                    channel_id = content[start:end]
                    if channel_id.startswith('UC'):
                        print(f"Found channel ID: {channel_id}")
                        return channel_id
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    
    # Fallback - you may need to manually set this
    return None

def fetch_youtube_videos_rss(channel_id=None):
    """Fetch videos from YouTube RSS feed"""
    if not channel_id:
        channel_id = get_channel_id()
    
    if not channel_id:
        print("Using hardcoded channel ID")
        # Faptured YouTube channel ID
        channel_id = "UCG2vySoJQ-vFheBqGmPnhIQ"
    
    # YouTube RSS feed URL
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    print(f"Fetching RSS feed from: {rss_url}")
    
    # Parse the feed
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        print("No videos found in RSS feed")
        return []
    
    videos = []
    for entry in feed.entries[:50]:  # Get up to 50 latest videos
        # Extract video ID from URL
        video_id = entry.yt_videoid if hasattr(entry, 'yt_videoid') else entry.link.split('watch?v=')[-1]
        
        video_data = {
            'id': video_id,
            'title': entry.title,
            'description': entry.summary[:200] + '...' if len(entry.summary) > 200 else entry.summary,
            'thumbnail': f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg",
            'publishedAt': entry.published,
            'url': entry.link,
            'author': entry.author if hasattr(entry, 'author') else 'faptured'
        }
        
        # Parse and format the date
        try:
            parsed_date = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%S+00:00')
            video_data['publishedAt'] = parsed_date.isoformat()
        except:
            pass
        
        videos.append(video_data)
    
    return videos

def save_videos_data(videos):
    """Save videos data to Jekyll data file"""
    data_dir = '_data'
    os.makedirs(data_dir, exist_ok=True)
    
    # Save as YAML for Jekyll
    with open(os.path.join(data_dir, 'youtube_videos.yml'), 'w') as f:
        yaml.dump({
            'videos': videos,
            'last_updated': datetime.now().isoformat(),
            'source': 'youtube_rss'
        }, f, default_flow_style=False, allow_unicode=True)
    
    print(f"Saved {len(videos)} videos to _data/youtube_videos.yml")

def main():
    try:
        videos = fetch_youtube_videos_rss()
        if videos:
            save_videos_data(videos)
        else:
            print("No videos found. Channel ID might need to be set manually.")
    except Exception as e:
        print(f"Error fetching videos: {e}")

if __name__ == "__main__":
    main()