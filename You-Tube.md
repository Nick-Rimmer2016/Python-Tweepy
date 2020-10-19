## You Tube & Twitter
### Random Notes to be organised
Get access to You Tube API v3, create a project and then enable the API and generate a key

Add You Tube client
pip3 install google-api-python-client
pip3 install emoji
pip3 install tweepy
pip3 install os 

Techsnips   
'channelId': 'UCFgZ8AxNf1Bd1C6V5-Vx7kA'

Pass Video list to videos array with channel id
videos = get_channel_videos('UCFgZ8AxNf1Bd1C6V5-Vx7kA')

Choose a random video
Import Random (into Python)
print(random.choice(videos))
randomvideo = (random.choice(videos))

Assign a variable to each
title = randomvideo["snippet"]["title"]
video = randomvideo['snippet']['resourceId']['videoId']

To be used in script https://www.youtube.com/watch?v=

Misc
result = 
for video in videos:
    print(video['snippet']['title'],video['snippet']['resourceId']['videoId'])