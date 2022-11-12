import tweepy
import os
import csv

class TweetGrabber():
    def __init__(self,myApi,sApi,at, sAt,client):
        self.client = tweepy.Client(client)
        auth = tweepy.OAuthHandler(myApi, sApi)
        auth.set_access_token(at, sAt)
        self.api = tweepy.API(auth)
     
		
	#Return the string without non ASCII characters
	# def strip_non_ascii(self,string):
		
	# 	stripped = (c for c in string if 0 < ord(c) < 127)
	# 	return ''.join(stripped)  
		
    def user_search(self,user):
        newUser = self.client.get_user(username=user)
        user_data = self.client.get_users_tweets(newUser.data.id,max_results = 10)
        return user_data

    
	# 	API_results = self.tweepy.Cursor(self.api.user_timeline,screen_name = user,tweet_mode='extended').items()

	# 	with open(f'{csv_prefix}.csv', 'w', newline='') as csvfile:
	# 		fieldnames = ['tweet_id', 'tweet_text', 'date', 'user_id', 'user_mentions', 'retweet_count']
	# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	# 		writer.writeheader()

	# 		for tweet in API_results:
	# 			text = self.strip_non_ascii(tweet.full_text)
	# 			date = tweet.created_at.strftime('%m/%d/%Y')        
	# 			writer.writerow({
	# 							'tweet_id': tweet.id_str,
	# 							'tweet_text': text,
	# 							'date': date,
	# 							'user_id': tweet.user.id_str,
	# 							'user_mentions':tweet.entities['user_mentions'],
	# 							'retweet_count': tweet.retweet_count
	# 							})
