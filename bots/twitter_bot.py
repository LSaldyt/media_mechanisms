#!/usr/bin/env python3
from twitter import *
from media import Media

def search(client, q, limit=100):
    return client.client.search.tweets(q=q)['statuses']

def create():
    with open('twitter.secret') as infile:
        api = Twitter(auth=OAuth(*infile.read().split()))
    return Media(api, search)
