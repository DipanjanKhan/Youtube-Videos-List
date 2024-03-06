from googleapiclient.discovery import build

api_key = 'AIzaSyCnqo23cenoVkiXoYJ93mRoaC9e56N3psM'
channelName = 'Technical Guruji'

def findChannelId(channelName):
    youtube = build('youtube', 'v3', developerKey = api_key)
    request = youtube.search().list(
        part = 'snippet',
        q = channelName,
        type = 'channel',
        maxResults = 1
    )
    response = request.execute()
    for i in response['items']:
        channel_id = i['id']['channelId']
    return channel_id

def findLeatestVideos(channel_id):
    youtube = build('youtube', 'v3', developerKey = api_key)
    request = youtube.search().list(
        part = 'snippet',
        channelId = channel_id,
        order = 'date',
        type = 'video',
        maxResults = 5,
    )
    respance = request.execute()
    num = 1
    for video in respance['items']:
        name = video['snippet']['title']
        thambnailUrl = video['snippet']['thumbnails']['high']['url']
        description = video['snippet']['description']
        publishedAt = video['snippet']['publishedAt']
        videoId = video['id']['videoId']
        videoUrl = f'https://youtube.com/watch?v={videoId}'
        print(f"Video {num}\nName: {name}\nThumbnail Url: {thambnailUrl}\nDescreption: {description}\nPublish At: {publishedAt}\nVideo Link: {videoUrl}\n")
        num += 1

if __name__ == '__main__':
    print(f"Channel Name: {channelName}\n")
    channel_id = findChannelId(channelName)
    findLeatestVideos(channel_id)