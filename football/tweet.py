#!/usr/bin/env python2.7  
# tweet.py by Alex Eames http://raspi.tv/?p=5908    
import tweepy  
import sys  
import config  
  
# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)  
auth.set_access_token(config.access_token, config.access_token_secret)  
   
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
  

def send_tweet_img(msg, file):
	if len(msg) <= 140:
		api.update_with_media(file, status=msg)
	else:
		print "tweet not sent. Too long. 140 chars Max."

def send_tweet(msg):

	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)

	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)

	if len(msg) <= 140:  
    		api.update_status(status=msg)  
	else:  
    		print "tweet not sent. Too long. 140 chars Max." 

	
