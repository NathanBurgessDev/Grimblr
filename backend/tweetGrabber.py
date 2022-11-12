import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

access_token =os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print(access_token + access_token_secret + consumer_key + consumer_secret)