from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import tweepy
import re
import tqdm
import cohere
import numpy as np
from datasets import load_dataset
from tweetGrabber import TweetGrabber
import os
import umap
import altair as alt
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import warnings
from annoy import AnnoyIndex
warnings.filterwarnings('ignore')
pd.set_option('display.max_colwidth', None)

load_dotenv()
cohere_key= os.getenv('cohere_key')
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
    tweetslist=[]
    username= request.json
    
   
    print(username)
    user=t.user_search(username)
    for i in user.data:
            print(i['text'])
            tweetslist.append(i['text'])
            length=len(tweetslist)
    df = pd.DataFrame (tweetslist, columns=['tweet'])
    co= cohere.Client(cohere_key)
    embeds= co.embed(texts=list(df['tweet']), model='large',
    truncate='LEFT').embeddings
    embeds=np.array(embeds)
    embeds.shape

    search_index = AnnoyIndex(embeds.shape[1], 'angular')

    for i in range(len(embeds)):
        search_index.add_item(i, embeds[i])
    search_index.build(10)
    search_index.save('test.ann')
    design_patterns=['observer bystander onlooker viewer watcher witness','singleton body individual article existence single', 'factory branch cooperative laboratory shop workshop', 'facade colour exterior front veneer disguise', 'strategy design method plan procedure method', 'builder architect contractor inventor manufacturer ', 'adapter connection bond fastener junction link', 'decorator fashion art creativity paint draw', 'abstract factory conglomerate capitalism production branches', 'iterator repetitive emphasize numerous again recurrent', 'flyweight minimal sharing sustainable caring support']
    min=None
    mini=0
    j=0
    for i in design_patterns:
        query_embed = co.embed(texts=[i], model="large", truncate="LEFT").embeddings
        similar_item_ids=search_index.get_nns_by_vector(query_embed[0], 10, include_distances=True)
        results = pd.DataFrame(data={'texts': df.iloc[similar_item_ids[0]]['tweet'], 
                             'distance': similar_item_ids[1]})
        
        df2=results["distance"].mean()
        print(i[0:10]+": "+str(df2))
        if min==None:
            min=df2
        if df2<=min:

            min=df2
            mini=j
        j+=1
    name=design_patterns[mini].split(" ")
    name=name[0]
    print("Your design pattern is:" + name)
    return username

if __name__== '__main__':
   app.run(host='0.0.0.0',port=5000)
    


