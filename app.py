
from flask import Flask, render_template , request,redirect

from main import main
from scripts.data_collection.youtube_data_collection import youtube_data_collection
from scripts.data_processing.youtube_data_processing import video_details_file_processing,comments_file_processing
import json

app = Flask(__name__)

import pandas as pd
folder_path='data/processed/'

def data_read():
    video_df= pd.read_csv(folder_path+'Vedio_details_processed.csv')
    return video_df


@app.route('/dashboard/<string:topic>')
def dashboard(topic):
    video_df= data_read()
    dict_video_df= video_df[video_df['topic']==topic].to_dict(orient='records')
    total_views = video_df[video_df['topic']==topic]['viewCount'].sum() #sum([i['views'] for i in videos])
    total_comments = video_df[video_df['topic']==topic]['commentCount'].sum() #sum([i['comments'] for i in videos])
    total_likes = video_df[video_df['topic']==topic]['likeCount'].sum() #sum([i['likes'] for i in videos])
    metrics = [total_views,total_likes,total_comments]

    return render_template(
        'dashboard.html',
        videos=dict_video_df,
        metrics =metrics
    )

@app.route('/submit', methods=['POST'])
def submit():
    topic = request.form['textInput']
    main(topic)
    # dashboard(topic)
    return redirect("/dashboard/"+topic)

@app.route('/')
def home():
    # main('trending')
    video_df= data_read()
    dict_video_df= video_df[video_df['topic']=='trending'].to_dict(orient='records')
    for video in dict_video_df:
        if isinstance(video['thumbnails'], str):
            
            try:
                video['thumbnails'] = json.loads(video['thumbnails'].replace("'", '"'))
            except json.JSONDecodeError:
                video['thumbnails'] = {}

    print(video['thumbnails'])

    if not dict_video_df:
        return "trending data not collected"
    return render_template('index.html',videos = dict_video_df,flag=1)


if __name__ == '__main__':
    app.run(debug=True)

