from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import tweepy
import re
from tweetGrabber import TweetGrabber
import os
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')
client = os.getenv('client')

t = TweetGrabber(
    myApi = consumer_key,
    sApi = consumer_secret,
    at = access_token,
    sAt = access_token_secret,
    client = client )

app=Flask(__name__, static_folder='../frontend')
CORS(app)
@app.route('/result', methods = ['POST'])
def result():
    username= request.json
    
   
    print(username)
    userid=t.user_id(username)
    userid=userid.data['id']
    
    return userid

if __name__== '__main__':
   app.run(host='0.0.0.0',port=5000)
    


