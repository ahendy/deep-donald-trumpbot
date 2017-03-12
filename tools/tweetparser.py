import twitter
from twitter import TwitterError
import time
from config import (
    TWITTER_CONSUMER_KEY,
    TWITTER_CONSUMER_SECRET,
    TWITTER_ACCESS_TOKEN_KEY,
    TWITTER_ACCESS_TOKEN_SECRET,
)

api = twitter.Api(
        consumer_key=TWITTER_CONSUMER_KEY,
        consumer_secret=TWITTER_CONSUMER_SECRET,
        access_token_key=TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
)

NAME = '@realDonaldTrump'
MAX_TWEETS = 35000
fname = 'deeptrump3'
file = '.'.join([fname, 'txt'])
#680492103722479616
def get_tweet(tweet_count=0, MAX_TWEETS=0, MAX_ID=680153902952615936):
    try:
        with open(file, 'a') as f:

            """Use 'a' for append"""
            while True:
                statuses = api.GetUserTimeline(screen_name=NAME, max_id=MAX_ID)
                num_tweets = len(statuses)
                MAX_TWEETS += num_tweets

                if num_tweets == 0:
                    # No more tweets
                    break
                
                MAX_ID = min(statuses, key=lambda x: x.id).id
                for status in statuses:
                    
                    try:
                        f.write(status.text + '\n')

                    except UnicodeEncodeError as e:
                        # Ignore ascii for now
                        unicode_str = status.text.encode('ascii', 'ignore')
                        f.write(unicode_str + '\n')
                    
                    else:
                        tweet_count += 1 

                print "%d/%d tweets written" % (tweet_count, MAX_TWEETS)
        
    except TwitterError as e:
        print e
        print "Possibly no more api requests"
        print "wait 15 minutes"

        time.sleep(62*15)
        get_tweet(tweet_count, MAX_TWEETS, MAX_ID)

    except KeyboardInterrupt:
        # Safely exit from ctrl-c
        pass

    print "LAST WRITTEN ID: ", MAX_ID 




if __name__=='__main__':
    get_tweet()
    print file, "finished writing"