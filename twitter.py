import tweepy
from tweepy import OAuthHandler
import json
import pymongo
import argparse
import configparser

class Twitter:
    class MyStreamListener(tweepy.StreamListener):
        def on_status(self, status):
            print(status.text)
        def on_data(self, data):
            client = pymongo.MongoClient("mongodb://localhost:27017")
            db = client['Twitter']
            col = db['tweets']

            datajson = json.loads(data)
            col.insert(datajson)
            #tweet_message = datajson['text']
            #print(tweet_message)

    consumer_key= 'hNJlx21hY5TVvnWosoCsxZ9d1'
    consumer_secret= 'SvoC6cRbemotiht0N6DNFWd0D4D8mNYgUMowHiSf2t8jjEUoE0'
    access_token= '2889340878-7AQ7okdh6yKpAE7Q100u7qFTNO4EGOw1mCVlA5o'
    access_token_secret= 'tSOMMGjasdmqGu3SfOVVpcaKJ6qIiVwcMrEq9LkzwcvLU'        

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['python'])
    
    
class test:
    a = Twitter()