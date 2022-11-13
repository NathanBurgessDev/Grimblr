from flask import Flask, request, send_from_directory
from flask_cors import CORS
import pandas as pd
import tweepy
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

app=Flask(__name__, static_folder='/build/static')
CORS(app)

@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/result', methods = ['POST'])
def result():
    username= request.data
    return username


if __name__== '__main__':
   ### USE FOR LOCAL TESTING ###
   # app.run(host='0.0.0.0',port=5000)
   app.run(use_reloader=True, port=5000, threaded=True)
    

client= tweepy.Client("AAAAAAAAAAAAAAAAAAAAAKHrjAEAAAAAGKRExYvQH7wUMuNi1yKkSQ12sjU%3DTvvpTvu4ZoV8dyHXdecJb5fqs0xJKnolipFHSfmaCC0Tjy90xW")
