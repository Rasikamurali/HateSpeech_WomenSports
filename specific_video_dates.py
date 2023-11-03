from googleapiclient.discovery import build
import pandas as pd
import json

api_key = "AIzaSyCAn1FLhH4yT0E1erGpqeDl6db4LjiWHhA"  # Replace with your API key
youtube = build('youtube', 'v3', developerKey=api_key)

# Define your search query
search_query = "womens wimbledon"

# Perform the channel search
search_response = youtube.search().list(
    q=search_query,
    type="channel",
    part="snippet",
    maxResults=1
).execute()

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

# Define the start and end date for filtering videos (in RFC3339 format)
start_date = "2023-07-01T00:00:00Z"
end_date = "2023-07-03T23:59:59Z"

# Create a function to collect video information and comments for a specific video
def collect_video_info(video_id):
    video_request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    video_response = video_request.execute()
    video_items = video_response.get("items", [])
    
    if not video_items:
        return None  # Video not found
    
    video_published_at = video_items[0]['snippet']['publishedAt']

    if start_date <= video_published_at <= end_date:
        video_snippet = video_items[0]['snippet']
        video_title = video_snippet['title']
        video_description = video_snippet['description']

        comments_request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            maxResults=1  # Adjust as needed to retrieve more comments
        )
        comments_response = comments_request.execute()
        comments_response_json = json.dumps(comments_response)
        comments_response_json = json.loads(comments_response_json)
        video_comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_response_json['items']]
        
        return {"id": video_id, "title": video_title, "description": video_description, "comments": video_comments}

    return None

# Collect video data for the specified channels
video_data = []
for channel_id in channel_ids:
    # Request video information from the channel
    videos_request = youtube.search().list(
        q="",
        channelId=channel_id,
        type="video",
        part="id",
        maxResults=1  # Adjust as needed to retrieve more videos
    )

    # Extract video IDs
    video_ids = [video['id']['videoId'] for video in videos_request.execute()['items']]

    # Retrieve video details and comments for videos published within the date range
    for vid in video_ids:
        video_info = collect_video_info(vid)
        if video_info:
            video_data.append(video_info)

# Create a DataFrame and save it to a CSV file
video_info = pd.DataFrame(video_data)
video_info.to_csv('womens_tennis_videos_and_comments_by_date1.csv', index=False)
