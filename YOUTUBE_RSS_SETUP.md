# YouTube RSS Integration (No API Key Required!)

This site automatically syncs with your YouTube channel using RSS feeds - no API key needed!

## How It Works

The GitHub Action fetches your YouTube RSS feed:
```
https://www.youtube.com/feeds/videos.xml?channel_id=UCG2vySoJQ-vFheBqGmPnhIQ
```

## Manual Trigger

1. Go to your repository's Actions tab
2. Select "Sync YouTube Videos via RSS"
3. Click "Run workflow"

## Automatic Updates

The workflow runs every 6 hours automatically. Videos are saved to `_data/youtube_videos.yml`.

## Test Locally

To test the script locally:
```bash
pip install feedparser pyyaml requests
python .github/scripts/fetch_youtube_rss.py
```

## Customization

- Change update frequency: Edit the cron schedule in `.github/workflows/youtube-rss-sync.yml`
- Limit number of videos: Edit `feed.entries[:50]` in the Python script
- Change data format: Modify the `video_data` structure in the script

## Benefits of RSS

- No API key required
- No rate limits
- Simple and reliable
- Works with any YouTube channel

## View Your Videos

Visit `/videos` on your site to see the synchronized YouTube videos!