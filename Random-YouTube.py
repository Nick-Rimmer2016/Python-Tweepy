import datetime
import tweepy
import random
import emoji
import os

# Setup Twitter API Access Using Secrets from GitHub
CONSUMER_KEY = os.environ['TWIT_CONS_KEY']
CONSUMER_SECRET = os.environ['TWIT_CONS_SEC']
ACCESS_TOKEN = os.environ['TWIT_ACC_TOK']
ACCESS_TOKEN_SECRET = os.environ['TWIT_ACC_SEC']

# Configure Tweepy to access Twitter
auth = tweepy.OAuth1UserHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')
    print(CONSUMER_KEY)

# Setup You Tube API Access
API_KEY = os.environ['API_KEY']
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=API_KEY)

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

# Construct tweet to publish
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
