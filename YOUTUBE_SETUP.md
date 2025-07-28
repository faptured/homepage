# YouTube Integration Setup

This site automatically syncs with your YouTube channel every 6 hours using GitHub Actions.

## Setup Instructions

### 1. Get a YouTube API Key

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable YouTube Data API v3
4. Create credentials → API Key
5. (Optional) Restrict the key to YouTube Data API v3

### 2. Add API Key to GitHub Secrets

1. Go to your repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `YOUTUBE_API_KEY`
4. Value: Your API key from step 1

### 3. Get Your Channel ID (if needed)

Your channel handle is @faptured, but if the script needs the UC... ID:

1. Go to your YouTube channel
2. View page source
3. Search for "channelId" or "UC"
4. Or use this tool: https://commentpicker.com/youtube-channel-id.php

Update the `CHANNEL_ID` in `.github/scripts/fetch_youtube_videos.py` if needed.

### 4. Run the Action

1. Go to Actions tab in your repository
2. Select "Sync YouTube Videos"
3. Click "Run workflow"

The action will:
- Fetch your latest videos
- Save them to `_data/youtube_videos.yml`
- Commit and push the changes
- Your site will rebuild automatically

## Automatic Updates

The workflow runs every 6 hours automatically. You can change this in `.github/workflows/youtube-sync.yml` by modifying the cron schedule.

## Alternative Options

### Option 1: YouTube RSS Feed (No API Key needed)
```javascript
// Simple RSS feed approach
const RSS_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID';
```

### Option 2: Manual Update
Simply edit `_data/youtube_videos.yml` manually with your video information.

### Option 3: Client-side JavaScript
Use YouTube's embed API to load videos dynamically in the browser.