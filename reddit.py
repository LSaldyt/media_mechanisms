import praw
from media import Media

def search(client, q, limit=100):
    return client.search(q, limit=n)

def create():
    reddit = praw.Reddit('analysis_bot', user_agent='lsaldyt')
    sub = reddit.subreddit('all')
    return Media(sub, search)

