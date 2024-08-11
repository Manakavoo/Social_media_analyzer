# import re
# from googleapiclient.discovery import build
# import csv
# from datetime import timedelta
# from urllib.parse import urlparse, parse_qs
# import os

# def get_video_id_from_url(url):
#     parsed_url = urlparse(url)
#     if parsed_url.hostname == 'youtu.be':
#         return parsed_url.path[1:]
#     elif parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
#         if parsed_url.path == '/watch':
#             return parse_qs(parsed_url.query).get('v', [None])[0]
#         elif parsed_url.path[:7] == '/embed/':
#             return parsed_url.path.split('/')[2]
#         elif parsed_url.path[:3] == '/v/':
#             return parsed_url.path.split('/')[2]
#         elif parsed_url.path[:8] == '/shorts/':
#             return parsed_url.path.split('/')[2]
#     return None

# def parse_duration(duration_str):
#     duration_pattern = re.compile(r'PT(\d+H)?(\d+M)?(\d+S)?')
#     match = duration_pattern.match(duration_str)
#     if match:
#         hours = int(match.group(1)[:-1]) if match.group(1) else 0
#         minutes = int(match.group(2)[:-1]) if match.group(2) else 0
#         seconds = int(match.group(3)[:-1]) if match.group(3) else 0
#         return timedelta(hours=hours, minutes=minutes, seconds=seconds)
#     return None

# API_KEY = "AIzaSyActb8A7PbAo5NpHlQ8SWi_i7GoIXP8lRk"
# folder_path = 'data/raw/youtube_data/'

# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# video_details_file = os.path.join(folder_path, 'video_details.csv')
# # VIDEO_URL = "https://youtu.be/Bi_Ot8_yDpo?si=2xdIjg9H3pCDlq_I"
# # VIDEO_URL ="https://youtu.be/fC5Er1VZKHc?si=ZdO2Q0OX4ry1afUc"

# # VIDEO_URL = "https://youtu.be/yZYrqa-K-qM?si=ZvhpqQyZ3STTFz9P"

# VIDEO_URL="https://youtu.be/gmPVSoHstxU?si=ShDI5oJUhICNg5er"

# VIDEO_ID = get_video_id_from_url(VIDEO_URL)

# if VIDEO_ID:
#     try:
#         youtube = build("youtube", "v3", developerKey=API_KEY)
#     except Exception as e:
#         print(f"Error creating YouTube API client: {e}")
#         exit(1)

#     try:
#         video_response = youtube.videos().list(
#             part="snippet,statistics,contentDetails",
#             id=VIDEO_ID
#         ).execute()
#     except Exception as e:
#         print(f"Error retrieving video details: {e}")
#         exit(1)

#     if not video_response["items"]:
#         print("No video details found for the provided video ID.")
#         exit(1)

#     video_details = video_response["items"][0]

#     video_kind = video_details['kind']

#     snippet = video_details.get("snippet", {})
#     video_publishedAt = snippet.get("publishedAt", "")
#     video_channel_id = snippet.get("channelId", "")
#     video_title = snippet.get("title", "")
#     video_description = snippet.get("description", "")
#     video_thumbnails = snippet.get("thumbnails", "")
#     video_channel_title = snippet.get("channelTitle", "")
#     video_categoryId = snippet.get("categoryId", "")
#     video_liveBroadcastContent = snippet.get("liveBroadcastContent", "")
#     video_defaultAudioLanguage = snippet.get("defaultAudioLanguage", "")
#     video_tags = snippet.get("tags", [])

#     content_details = video_details.get("contentDetails", {})
#     video_duration = content_details.get("duration", "")
#     video_dimension = content_details.get("dimension", "")
#     video_definition = content_details.get("definition", "")
#     video_caption = content_details.get("caption", "")
#     video_licensedContent = content_details.get("licensedContent", "")
#     video_contentRating = content_details.get("contentRating", "")
#     video_projection = content_details.get("projection", "")

#     statistics = video_details.get("statistics", {})
#     video_viewCount = statistics.get("viewCount", 0)
#     video_likeCount = statistics.get("likeCount", 0)
#     video_favoriteCount = statistics.get("favoriteCount", 0)
#     video_commentCount = statistics.get("commentCount", 0)

#     Total_fields = ['video_id', 'publishedAt', 'channelId', 'title', 'description', 'thumbnails', 'channelTitle', 'tags',
#                     'categoryId', 'liveBroadcastContent', 'defaultAudioLanguage', 'duration', 'dimension', 'definition', 'caption', 
#                     'licensedContent', 'contentRating', 'projection', 'viewCount', 'likeCount', 'favoriteCount', 'commentCount', 'kind']

#     try:
#         with open(video_details_file, mode="r", newline="", encoding="utf-8-sig") as file:
#             reader = csv.DictReader(file)
#             video_details_data = list(reader)
#     except FileNotFoundError:
#         video_details_data = []
#     except Exception as e:
#         print(f"Error reading video details file: {e}")
#         exit(1)

#     video_id_exists = any(row["video_id"] == VIDEO_ID for row in video_details_data)

#     try:
#         with open(video_details_file, mode="a", newline="", encoding="utf-8-sig") as file:
#             writer = csv.DictWriter(file, fieldnames=Total_fields)
#             if not video_details_data:
#                 writer.writeheader()

#             video_details_row = {
#                 "video_id": VIDEO_ID,
#                 "publishedAt": video_publishedAt,
#                 "channelId": video_channel_id,
#                 "title": video_title,
#                 "description": video_description,
#                 "thumbnails": video_thumbnails,
#                 "channelTitle": video_channel_title,
#                 "tags": ",".join(video_tags),
#                 "categoryId": video_categoryId,
#                 "liveBroadcastContent": video_liveBroadcastContent,
#                 "defaultAudioLanguage": video_defaultAudioLanguage,
#                 "duration": video_duration,
#                 "dimension": video_dimension,
#                 "definition": video_definition,
#                 "caption": video_caption,
#                 "licensedContent": video_licensedContent,
#                 "contentRating": video_contentRating,
#                 "projection": video_projection,
#                 "viewCount": video_viewCount,
#                 "likeCount": video_likeCount,
#                 "favoriteCount": video_favoriteCount,
#                 "commentCount": video_commentCount,
#                 "kind": video_kind
#             }

#             if video_id_exists:
#                 for i, row in enumerate(video_details_data):
#                     if row["video_id"] == VIDEO_ID:
#                         video_details_data[i] = video_details_row
#                         break
#             else:
#                 writer.writerow(video_details_row)
#                 video_details_data.append(video_details_row)

#         with open(video_details_file, mode="w", newline="", encoding="utf-8-sig") as file:
#             writer = csv.DictWriter(file, fieldnames=Total_fields)
#             writer.writeheader()
#             writer.writerows(video_details_data)

#     except Exception as e:
#         print(f"Error writing video details to file: {e}")
#         exit(1)

#     # Function to retrieve all comments
#     def retrieve_all_comments(youtube, video_id):
#         comments = []
#         next_page_token = None

#         while True:
#             try:
#                 comment_threads = youtube.commentThreads().list(
#                     part="snippet",
#                     videoId=video_id,
#                     maxResults=100,
#                     pageToken=next_page_token
#                 ).execute()
#             except Exception as e:
#                 print(f"Error retrieving video comments: {e}")
#                 break

#             for comment_thread in comment_threads.get("items", []):
#                 comment = comment_thread["snippet"]["topLevelComment"]["snippet"]
#                 timestamp = comment.get("publishedAt", "")
#                 comment_text = comment.get("textDisplay", "")
#                 comment_author = comment.get("authorDisplayName", "")
#                 like_count = comment.get("likeCount", 0)
#                 comments.append({
#                     "timestamp": timestamp, 
#                     "comment_text": comment_text, 
#                     "author": comment_author, 
#                     "like_count": like_count,
#                     "video_id": video_id
#                 })

#             next_page_token = comment_threads.get("nextPageToken")
#             if not next_page_token:
#                 break

#         return comments

#     comments = retrieve_all_comments(youtube, VIDEO_ID)

#     comment_file = os.path.join(folder_path, f"{video_channel_title}_{VIDEO_ID}.csv")

#     try:
#         with open(comment_file, mode="w", newline="", encoding="utf-8-sig") as file:
#             fieldnames = ["timestamp", "comment_text", "author", "like_count", "video_id"]
#             writer = csv.DictWriter(file, fieldnames=fieldnames)
#             writer.writeheader()
#             for comment in comments:
#                 writer.writerow(comment)
#     except Exception as e:
#         print(f"Error writing comments to file: {e}")
#         exit(1)

#     print(f"Video details ({video_details_file}) and comments ({comment_file}) have been saved for video ID: {VIDEO_ID}")
# else:
#     print("Invalid YouTube video URL")
# import re
# import csv
# import os
# from datetime import timedelta
# from urllib.parse import urlparse, parse_qs
# from googleapiclient.discovery import build

# def sanitize_filename(filename):
#     # Replace characters that are not allowed in filenames
#     return re.sub(r'[<>:"/\\|?*\x00-\x1F ]', '_', filename)

# def get_video_id_from_url(url):
#     parsed_url = urlparse(url)
#     if parsed_url.hostname == 'youtu.be':
#         return parsed_url.path[1:]
#     elif parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
#         if parsed_url.path == '/watch':
#             return parse_qs(parsed_url.query).get('v', [None])[0]
#         elif parsed_url.path[:7] == '/embed/':
#             return parsed_url.path.split('/')[2]
#         elif parsed_url.path[:3] == '/v/':
#             return parsed_url.path.split('/')[2]
#         elif parsed_url.path[:8] == '/shorts/':
#             return parsed_url.path.split('/')[2]
#     return None

# def parse_duration(duration_str):
#     duration_pattern = re.compile(r'PT(\d+H)?(\d+M)?(\d+S)?')
#     match = duration_pattern.match(duration_str)
#     if match:
#         hours = int(match.group(1)[:-1]) if match.group(1) else 0
#         minutes = int(match.group(2)[:-1]) if match.group(2) else 0
#         seconds = int(match.group(3)[:-1]) if match.group(3) else 0
#         return timedelta(hours=hours, minutes=minutes, seconds=seconds)
#     return None

# def search_videos_by_topic(youtube, query, max_results=3):
#     search_response = youtube.search().list(
#         part="snippet",
#         q=query,
#         type="video",
#         maxResults=max_results
#     ).execute()

#     video_ids = [item['id']['videoId'] for item in search_response['items']]
#     return video_ids

# def retrieve_video_details(youtube, video_id):
#     video_response = youtube.videos().list(
#         part="snippet,statistics,contentDetails",
#         id=video_id
#     ).execute()

#     if not video_response["items"]:
#         return None

#     video_details = video_response["items"][0]

#     snippet = video_details.get("snippet", {})
#     content_details = video_details.get("contentDetails", {})
#     statistics = video_details.get("statistics", {})

#     video_data = {
#         'video_id': video_id,
#         'publishedAt': snippet.get("publishedAt", ""),
#         'channelId': snippet.get("channelId", ""),
#         'title': snippet.get("title", ""),
#         'description': snippet.get("description", ""),
#         'thumbnails': snippet.get("thumbnails", ""),
#         'channelTitle': snippet.get("channelTitle", ""),
#         'tags': ",".join(snippet.get("tags", [])),
#         'categoryId': snippet.get("categoryId", ""),
#         'liveBroadcastContent': snippet.get("liveBroadcastContent", ""),
#         'defaultAudioLanguage': snippet.get("defaultAudioLanguage", ""),
#         'duration': content_details.get("duration", ""),
#         'dimension': content_details.get("dimension", ""),
#         'definition': content_details.get("definition", ""),
#         'caption': content_details.get("caption", ""),
#         'licensedContent': content_details.get("licensedContent", ""),
#         'contentRating': content_details.get("contentRating", ""),
#         'projection': content_details.get("projection", ""),
#         'viewCount': statistics.get("viewCount", 0),
#         'likeCount': statistics.get("likeCount", 0),
#         'favoriteCount': statistics.get("favoriteCount", 0),
#         'commentCount': statistics.get("commentCount", 0)
#     }

#     return video_data

# def retrieve_all_comments(youtube, video_id):
#     comments = []
#     next_page_token = None

#     while True:
#         try:
#             comment_threads = youtube.commentThreads().list(
#                 part="snippet",
#                 videoId=video_id,
#                 maxResults=100,
#                 pageToken=next_page_token
#             ).execute()
#         except Exception as e:
#             error_details = e.resp.json().get('error', {}).get('errors', [])
#             for error in error_details:
#                 if error.get('reason') == 'commentsDisabled':
#                     print(f"Comments are disabled for videoId: {video_id}.")
#                     break
#             print(f"An error occurred: {e}")
#             # print(f"Error retrieving video comments: {type(e)}\n")
#             break

#         if "items" not in comment_threads:
#             print(f"No comments found or error retrieving comments for video ID: {video_id}\n")
#             break

#         for comment_thread in comment_threads.get("items", []):
#             comment = comment_thread["snippet"]["topLevelComment"]["snippet"]
#             comments.append({
#                 "timestamp": comment.get("publishedAt", ""),
#                 "comment_text": comment.get("textDisplay", ""),
#                 "author": comment.get("authorDisplayName", ""),
#                 "like_count": comment.get("likeCount", 0),
#                 "video_id": video_id
#             })

#         next_page_token = comment_threads.get("nextPageToken")
#         if not next_page_token:
#             break

#     return comments

# def save_to_csv(file_path, data, fieldnames):
#     with open(file_path, mode="w", newline="", encoding="utf-8-sig") as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)

# API_KEY = "AIzaSyActb8A7PbAo5NpHlQ8SWi_i7GoIXP8lRk"
# folder_path = 'data/raw/youtube_data/'

# youtube = build("youtube", "v3", developerKey=API_KEY)
# topic = "Machine_learning"
# video_ids = search_videos_by_topic(youtube, topic, max_results=5)
# folder_path_topic = 'data/raw/youtube_data/'+str(sanitize_filename(topic))

# if not os.path.exists(folder_path_topic):
#     os.makedirs(folder_path_topic)

# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# video_details_list = []
# for video_id in video_ids:
#     video_details = retrieve_video_details(youtube, video_id)
#     if video_details:
#         video_details_list.append(video_details)
#         try:
#             comments = retrieve_all_comments(youtube, video_id)
#             # Sanitize the video title for use in the filename
#             sanitized_title = sanitize_filename(video_details['title'])
#             comment_file = os.path.join(folder_path_topic, f"{sanitized_title}_{video_id}.csv")
#             save_to_csv(comment_file, comments, ["timestamp", "comment_text", "author", "like_count", "video_id"])
#         except Exception as e:
#             print(f"Skipping comments for video ID {video_id} due to error: {e}")

# # Sanitize the file path for the video details CSV
# video_details_file = os.path.join(folder_path, 'Video_Details.csv')
# save_to_csv(video_details_file, video_details_list, [
#     'video_id', 'publishedAt', 'channelId', 'title', 'description', 'thumbnails', 'channelTitle',
#     'tags', 'categoryId', 'liveBroadcastContent', 'defaultAudioLanguage', 'duration', 'dimension',
#     'definition', 'caption', 'licensedContent', 'contentRating', 'projection', 'viewCount',
#     'likeCount', 'favoriteCount', 'commentCount'
# ])

# print(f"Video details and comments have been saved for topic: {topic}")

import re
import csv
import os
from datetime import timedelta
from urllib.parse import urlparse, parse_qs
from googleapiclient.discovery import build

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*\x00-\x1F ]', '_', filename)

def get_video_id_from_url(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    elif parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif parsed_url.path[:7] == '/embed/':
            return parsed_url.path.split('/')[2]
        elif parsed_url.path[:3] == '/v/':
            return parsed_url.path.split('/')[2]
        elif parsed_url.path[:8] == '/shorts/':
            return parsed_url.path.split('/')[2]
    return None

def parse_duration(duration_str):
    duration_pattern = re.compile(r'PT(\d+H)?(\d+M)?(\d+S)?')
    match = duration_pattern.match(duration_str)
    if match:
        hours = int(match.group(1)[:-1]) if match.group(1) else 0
        minutes = int(match.group(2)[:-1]) if match.group(2) else 0
        seconds = int(match.group(3)[:-1]) if match.group(3) else 0
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return None

def search_videos_by_topic(youtube, query, max_results=3):
    search_response = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return video_ids

def retrieve_video_details(youtube, video_id):
    video_response = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    ).execute()

    if not video_response["items"]:
        return None

    video_details = video_response["items"][0]

    snippet = video_details.get("snippet", {})
    content_details = video_details.get("contentDetails", {})
    statistics = video_details.get("statistics", {})

    video_data = {
        
        'video_id': video_id,
        'publishedAt': snippet.get("publishedAt", ""),
        'channelId': snippet.get("channelId", ""),
        'title': snippet.get("title", ""),
        'description': snippet.get("description", ""),
        'thumbnails': snippet.get("thumbnails", ""),
        'channelTitle': snippet.get("channelTitle", ""),
        'tags': ",".join(snippet.get("tags", [])),
        'categoryId': snippet.get("categoryId", ""),
        'liveBroadcastContent': snippet.get("liveBroadcastContent", ""),
        'defaultAudioLanguage': snippet.get("defaultAudioLanguage", ""),
        'duration': content_details.get("duration", ""),
        'dimension': content_details.get("dimension", ""),
        'definition': content_details.get("definition", ""),
        'caption': content_details.get("caption", ""),
        'licensedContent': content_details.get("licensedContent", ""),
        'contentRating': content_details.get("contentRating", ""),
        'projection': content_details.get("projection", ""),
        'viewCount': statistics.get("viewCount", 0),
        'likeCount': statistics.get("likeCount", 0),
        'favoriteCount': statistics.get("favoriteCount", 0),
        'commentCount': statistics.get("commentCount", 0)
    }

    return video_data

def retrieve_all_comments(youtube, video_id):
    comments = []
    next_page_token = None

    while True:
        try:
            comment_threads = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            ).execute()
        except Exception as e:
            error_details = e.resp.json().get('error', {}).get('errors', [])
            for error in error_details:
                if error.get('reason') == 'commentsDisabled':
                    print(f"Comments are disabled for videoId: {video_id}.")
                    break
            print(f"An error occurred: {e}")
            break


        if "items" not in comment_threads:
            print(f"No comments found or error retrieving comments for video ID: {video_id}\n")
            break

        for comment_thread in comment_threads.get("items", []):
            comment = comment_thread["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "timestamp": comment.get("publishedAt", ""),
                "comment_text": comment.get("textDisplay", ""),
                "author": comment.get("authorDisplayName", ""),
                "like_count": comment.get("likeCount", 0),
                "video_id": video_id
            })

        next_page_token = comment_threads.get("nextPageToken")
        if not next_page_token:
            break

    return comments

def load_existing_data(file_path, key_field):
    existing_data = {}
    if os.path.exists(file_path):
        with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_data[row[key_field]] = row
    return existing_data

def save_to_csv(file_path, data, fieldnames, key_field):
    existing_data = load_existing_data(file_path, key_field)
    
    # Update existing data with new data
    for item in data:
        key = item[key_field]
        if key in existing_data:
            existing_data[key].update(item)
        else:
            existing_data[key] = item

    with open(file_path, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data.values())

API_KEY = "AIzaSyActb8A7PbAo5NpHlQ8SWi_i7GoIXP8lRk"
folder_path = 'data/raw/youtube_data/'

youtube = build("youtube", "v3", developerKey=API_KEY)
topic = "tamil"
topic= sanitize_filename(topic)
video_ids = search_videos_by_topic(youtube, topic, max_results=5)
folder_path_topic = 'data/raw/youtube_data/'+str(topic)

if not os.path.exists(folder_path_topic):
    os.makedirs(folder_path_topic)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

video_details_list = []
for video_id in video_ids:
    video_details = retrieve_video_details(youtube, video_id)
    if video_details:
        video_details_list.append(video_details)
        try:
            comments = retrieve_all_comments(youtube, video_id)
            sanitized_title = sanitize_filename(video_details['title'])
            comment_file = os.path.join(folder_path_topic, f"{sanitized_title}_{video_id}.csv")
            save_to_csv(comment_file, comments, ["timestamp", "comment_text", "author", "like_count", "video_id"], "timestamp")
        except Exception as e:
            print(f"Skipping comments for video ID {video_id} due to error: {e}")

video_details_file = os.path.join(folder_path, 'Video_Details.csv')
save_to_csv(video_details_file, video_details_list, [
    'video_id', 'publishedAt', 'channelId', 'title', 'description', 'thumbnails', 'channelTitle',
    'tags', 'categoryId', 'liveBroadcastContent', 'defaultAudioLanguage', 'duration', 'dimension',
    'definition', 'caption', 'licensedContent', 'contentRating', 'projection', 'viewCount',
    'likeCount', 'favoriteCount', 'commentCount'
], 'video_id')


print(f"Video details and comments have been updated for topic: {topic}")
