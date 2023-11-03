from googleapiclient.discovery import build
import pandas as pd 
# Set your API key
<<<<<<< HEAD
#api_key = "AIzaSyCwjeIC7jXp9DTj021DsvF0H_k9QjEZ294"
=======
api_key = "***"
>>>>>>> 1c6e4917a400c10bc246d8d5252caded634543db

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

def search_resp(search_query, maxResults): 
    search_response = youtube.search().list(
    q=search_query,
    type="channel",
    part="snippet", 
    maxResults = 1 # Include the "snippet" part
).execute()
    return search_response


# # Define your search query
# search_query = "espn women"

# # Perform the channel search
# search_response = youtube.search().list(
#     q=search_query,
#     type="channel",
#     part="snippet", 
#     maxResults = 20 # Include the "snippet" part
# ).execute()

# Extract the channel information

def channels(search_response): 
    for search_result in search_response.get("items", []):
        channel_id = search_result["id"]["channelId"]
        channel_title = search_result["snippet"]["title"]
        channels.append({"id": channel_id, "title": channel_title})
        channel_ids = []
        for channel in channels:
            channel_ids.append(channel['id'])
            print(f"Channel ID: {channel['id']}, Title: {channel['title']}")
    return channel_ids


# channels = []
# for search_result in search_response.get("items", []):
#     channel_id = search_result["id"]["channelId"]
#     channel_title = search_result["snippet"]["title"]
#     channels.append({"id": channel_id, "title": channel_title})

# # Print the list of sports channels
# channel_ids = []
# for channel in channels:
#     channel_ids.append(channel['id'])
#     print(f"Channel ID: {channel['id']}, Title: {channel['title']}")

def videos(channel_ids): 
    for id in channel_ids: 
    # Request video information from the channel
        videos_request = youtube.search().list(
            q="",
            channelId=id,
            type="video",
            part="id",
            maxResults=1  # Adjust as needed to retrieve more videos
        )

    # Extract video IDs
    video_ids = [video['id']['videoId'] for video in videos_request.execute()['items']]

# for id in channel_ids: 
#     # Request video information from the channel
#     videos_request = youtube.search().list(
#         q="",
#         channelId=channel_id,
#         type="video",
#         part="id",
#         maxResults=20  # Adjust as needed to retrieve more videos
#     )

#     # Extract video IDs
#     video_ids = [video['id']['videoId'] for video in videos_request.execute()['items']]
# #print(video_ids)

# video_data = []
# for vid in video_ids: 
#     video_request = youtube.videos().list(
#         part="snippet",
#         id=vid
#     )
#     video_response = video_request.execute()
#     video_snippet = video_response['items'][0]['snippet']
#     video_title = video_snippet['title']
#     video_description = video_snippet['description']

#     # Get video comments
#     comments_request = youtube.commentThreads().list(
#         part="snippet",
#         videoId=vid,
#         textFormat="plainText",
#         maxResults=10  # Adjust as needed to retrieve more comments
#     )
#     comments_response = comments_request.execute()
#     #print(comments_response)
#     video_comments = [comment['snippet']['topLevelComment']['snippet']['textDisplay'] for comment in comments_response['items']]
#     print(video_comments)
#     video_data.append({"id": vid, "title": video_title, "description": video_description, "comments": video_comments})

# video_info = pd.DataFrame(video_data)
# #print(video_info.head())