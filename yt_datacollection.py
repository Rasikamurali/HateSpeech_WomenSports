from googleapiclient.discovery import build
import pandas as pd 
# Set your API key
api_key = "***"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Define your search query
search_query = "espn women"

# Perform the channel search
search_response = youtube.search().list(
    q=search_query,
    type="channel",
    part="snippet"  # Include the "snippet" part
).execute()

# Extract the channel information
channels = []
for search_result in search_response.get("items", []):
    channel_id = search_result["id"]["channelId"]
    channel_title = search_result["snippet"]["title"]
    channels.append({"id": channel_id, "title": channel_title})

# Print the list of sports channels
channel_ids = []
for channel in channels:
    channel_ids.append(channel['id'])
    print(f"Channel ID: {channel['id']}, Title: {channel['title']}")

print(channel_ids)
for id in channel_ids: 
    # Request video information from the channel
    videos_request = youtube.search().list(
        q="",
        channelId=channel_id,
        type="video",
        part="id",
        maxResults=2  # Adjust as needed to retrieve more videos
    )

    # Extract video IDs
    video_ids = [video['id']['videoId'] for video in videos_request.execute()['items']]
print(video_ids)

video_data = []
for vid in video_ids: 
    video_request = youtube.videos().list(
        part="snippet",
        id=vid
    )
    video_response = video_request.execute()
    video_snippet = video_response['items'][0]['snippet']
    video_title = video_snippet['title']
    video_description = video_snippet['description']

    # Get video comments
    comments_request = youtube.commentThreads().list(
        part="snippet",
        videoId=vid,
        textFormat="plainText",
        maxResults=100  # Adjust as needed to retrieve more comments
    )
    comments_response = comments_request.execute()
    video_comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_response['items']]

    video_data.append({"id": vid, "title": video_title, "description": video_description, "comments": video_comments})

video_info = pd.DataFrame(video_data)
