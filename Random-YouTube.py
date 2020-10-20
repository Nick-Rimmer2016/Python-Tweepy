import datetime
import tweepy
import random
import emoji
import os

# Setup Twitter API Access Using Secrets from Jenkins, otherwise add manually. Be careful !
consumer_key = os.getenv("twit_cons_key")
consumer_secret = os.getenv("twit_cons_sec")
access_token = os.getenv("twit_acc_tok")
access_token_secret = os.getenv("twit_acc_sec")

# Configure Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Setup You Tube API Access
api_key = os.getenv("api_key")
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)

# Retrieve a list of videos using channel ID (courtesy of @IndPythonnista)
def get_channel_videos(channel_id):
    
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

# Construct tweet 
def publictweet():
    
    videos = get_channel_videos('UCFgZ8AxNf1Bd1C6V5-Vx7kA')
    randomvideo = (random.choice(videos))

    emo = (emoji.emojize(':thumbs_up:'))
    subtitle = "Another Great Video from TechSnips!\n @techsnips_io"
    video = randomvideo['snippet']['resourceId']['videoId']
    title = randomvideo["snippet"]["title"]
    tweettopublish = title + "\nhttps://www.youtube.com/watch?v=" + video + "\n" + subtitle + emo + "\n" + "#techsnipsTuesday"

    api.update_status(tweettopublish)
    print(tweettopublish)

publictweet()
