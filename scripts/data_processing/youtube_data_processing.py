import pandas as pd
import re
import os
src_folder_path='data/raw/'
save_folder_path ='data/processed/'


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


def video_details_file_processing():
    if not os.path.exists(src_folder_path):
        os.mkdir(src_folder_path)
    
    video_file_path ="video_details.csv"
    video_df = pd.read_csv(src_folder_path+video_file_path)
    video_df.fillna(value='None', inplace=True) 

    video_categories = {
        1: "Film & Animation",2: "Autos & Vehicles",10: "Music",15: "Pets & Animals",17: "Sports",18: "Short Movies",19: "Travel & Events",20: "Gaming",
        21: "Videoblogging",22: "People & Blogs",23: "Comedy",24: "Entertainment",25: "News & Politics",26: "Howto & Style",27: "Education",
        28: "Science & Technology",29: "Nonprofits & Activism",30: "Movies",31: "Anime/Animation",32: "Action/Adventure",33: "Classics",34: "Comedy",35: "Documentary",
        36: "Drama",37: "Family",38: "Foreign",39: "Horror",40: "Sci-Fi/Fantasy",41: "Thriller",42: "Shorts",43: "Shows",44: "Trailers"
    }

    video_df['video_link']="https://www.youtube.com/watch?v="+video_df['video_id']
    video_df['publishedDate'] = pd.to_datetime(video_df['publishedAt']).dt.strftime('%d-%m-%y')
    video_df['publishedTime'] = pd.to_datetime(video_df['publishedAt']).dt.strftime('%H:%M:%S')
    # video_df['time_duration'] = video_df['duration'].apply(duration_)
    video_df['categoryName'] = video_df['categoryId'].map(video_categories)
    video_df['liveBroadcastContent'] = "None"

    # print(video_df.shape)
    # col= ['video_id', 'channelId', 'channelTitle', 'title', 'publishedAt',
    #     'viewCount', 'likeCount', 'favoriteCount', 'commentCount', 'duration',
    #     'description', 'tags', 'thumbnails', 'projection', 'categoryId',
    #     'caption', 'licensedContent', 'defaultAudioLanguage', 'dimension',
    #     'definition', 'contentRating', 'liveBroadcastContent', 'video_link',
    #     'publishedDate', 'publishedTime', 'time_duration', 'categoryName']
    if not os.path.exists(save_folder_path):
        os.mkdir(save_folder_path)
    video_df.to_csv(save_folder_path+'Vedio_details_processed.csv',index=True,index_label='Sno')
    print("Video details data Processed sucessfully...")
    return None

def comments_file_processing(topic:str):
    for i in os.listdir(src_folder_path):
        if i!="Video_Details.csv":
            comments_file=os.listdir(src_folder_path+i)
            comment_file_path=save_folder_path+i+"/" 

            if topic==i:
                for j in comments_file:
                    # print(i,j)
                    #save_folder_path ='data/processed/'
                    comment_df = pd.read_csv(src_folder_path+i+"/"+j)
                    comment_df['time_duration'] = pd.to_datetime(comment_df['timestamp']).dt.strftime('%H:%M:%S')
                    comment_df['date'] = pd.to_datetime(comment_df['timestamp']).dt.strftime('%d-%m-%y')
                    comment_df.fillna(value='None', inplace=True)

                    if not os.path.exists(comment_file_path):
                        os.mkdir(comment_file_path)
                    comment_df.to_csv(comment_file_path+j,index=True,index_label="Sno")
                print(f"{i} comments folder data processed sucessfully....")

    return None

# video_details_file_processing()

# comments_file_processing('vijay')


