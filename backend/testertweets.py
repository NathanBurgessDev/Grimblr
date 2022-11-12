from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import tweepy

app=Flask(__name__, static_folder='../frontend')
CORS(app)
@app.route('/result', methods = ['POST'])
def result():
    username= request.data
    return username

if __name__== '__main__':
   app.run(host='0.0.0.0',port=5000)
    

client= tweepy.Client("AAAAAAAAAAAAAAAAAAAAAKHrjAEAAAAAGKRExYvQH7wUMuNi1yKkSQ12sjU%3DTvvpTvu4ZoV8dyHXdecJb5fqs0xJKnolipFHSfmaCC0Tjy90xW")


user= client.get_users_tweets(1339289068832763908, max_results=5)

for data in user.data:
    print(data['text'])