from scripts.data_collection.youtube_data_collection import youtube_data_collection
from scripts.data_processing.youtube_data_processing import video_details_file_processing,comments_file_processing

def main(topic:str ='doraemon'):
    x=youtube_data_collection(topic,2)

    video_details_file_processing()
    comments_file_processing(x)
    print("main funtion exeuted")

# if __name__=="__main__":
#     main()

