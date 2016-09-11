import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import json

from config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN_KEY,
    TWITTER_ACCESS_TOKEN_SECRET,
)

consumer_key = TWITTER_CONSUMER_KEY
consumer_secret = TWITTER_CONSUMER_SECRET
access_token = TWITTER_ACCESS_TOKEN_KEY
access_secret = TWITTER_ACCESS_TOKEN_SECRET
 


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def on_data(self, data):
        try:
            with open("trumpstream.txt", 'a') as f:
                all_data = json.loads(data)
                tweet = all_data['text']

                import pdb;pdb.set_trace()
                f.write(data)
                print(data)
                return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
 

    api = tweepy.API(auth)
    user = api.get_user('realDonaldTrump')
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter()