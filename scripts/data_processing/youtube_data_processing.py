import pandas as pd
import numpy as np
import re
# import matplotlib.pyplot as plt
folder_path="data/raw/youtube_data/"
video_file_path ="video_details.csv"
video_df = pd.read_csv(folder_path+video_file_path)

video_df.fillna(value='None', inplace=True)

video_categories = {
    1: "Film & Animation",2: "Autos & Vehicles",10: "Music",15: "Pets & Animals",17: "Sports",18: "Short Movies",19: "Travel & Events",20: "Gaming",
    21: "Videoblogging",22: "People & Blogs",23: "Comedy",24: "Entertainment",25: "News & Politics",26: "Howto & Style",27: "Education",
    28: "Science & Technology",29: "Nonprofits & Activism",30: "Movies",31: "Anime/Animation",32: "Action/Adventure",33: "Classics",34: "Comedy",35: "Documentary",
    36: "Drama",37: "Family",38: "Foreign",39: "Horror",40: "Sci-Fi/Fantasy",41: "Thriller",42: "Shorts",43: "Shows",44: "Trailers"
}
def duration_(duration):
    if not duration:
        return None
    pattern = re.compile("PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)")
    match = pattern.match(duration)
    hour= match.group(1) or 0
    min=match.group(2) or 0
    sec=match.group(3) or 0
    time=str(hour)+":"+str(min)+":"+str(sec)
    # print(time)
    return time

video_df['video_link']="https://www.youtube.com/watch?v="+video_df['video_id']
video_df['publishedDate'] = pd.to_datetime(video_df['publishedAt']).dt.strftime('%d-%m-%y')
video_df['publishedTime'] = pd.to_datetime(video_df['publishedAt']).dt.strftime('%H:%M:%S')
video_df['time_duration'] = video_df['duration'].apply(duration_)
video_df['categoryName'] = video_df['categoryId'].map(video_categories)
video_df['liveBroadcastContent'] = "None"
# print(video_df.columns)
# print(video_df.info())
# print(video_df['video_link'])
# print(video_df.isnull().sum()/len(video_df)*100)
# print(video_df['publishedAt'].head(3))
# print(video_df['duration'].head(3))
# print()
# print(video_df['time_duration'].head(3))

# print(video_df['categoryName'].unique())
# print(video_df['categoryId'].unique())
# for i in video_df['categoryId'].unique().tolist():
#     print(i,video_df[video_df["categoryId"]==i]['channelTitle'].unique().tolist())

print(video_df.shape)
col= ['video_id', 'channelId', 'channelTitle', 'title', 'publishedAt',
       'viewCount', 'likeCount', 'favoriteCount', 'commentCount', 'duration',
       'description', 'tags', 'thumbnails', 'projection', 'categoryId',
       'caption', 'licensedContent', 'defaultAudioLanguage', 'dimension',
       'definition', 'contentRating', 'liveBroadcastContent', 'video_link',
       'publishedDate', 'publishedTime', 'time_duration', 'categoryName']

video_df.to_csv('data/processed/vedio_details_processed.csv',index=True,index_label='Sno')


