##############################################################################################
# Made in 2016 by Flora M. Rosenkreuz
# Follow me on twitter: @yung_jiggly
# Honestly, I really don't care what you do with this, as long as you don't claim you made it.
# If you use it, link back to the github page, so other people can, too.
# Or you can expand on this and do whatever for yourself, I don't mind.
##############################################################################################

import time
import requests
import tweepy
import urllib
import os
import random

page = 1
# Edit the tags=. It's only limited to two tags, though.
url = 'https://danbooru.donmai.us/posts.json?tags=example_tag_1 example_tag_2&limit=10&page='
# Enter your twitter credentials here, as strings.
consumer_key = 
consumer_secret = 
access_key = 
access_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)
		
while True:
	try:
		random.seed()
		jsURL = url + str(random.randint(1,1000))
		response = requests.get(jsURL)
		pageTable = response.json()
		arrayNum = random.randint(0,9)
		
		# If you want to expand on this,
		# https://danbooru.donmai.us/posts.json?tags=yakumo_ran&page=1000&limit=1
		# is an example post json table.
		imageSource = pageTable[arrayNum]["file_url"]
		imageURL = "http://danbooru.donmai.us" + imageSource
		print imageURL
		sourceURL = "http://danbooru.donmai.us/posts/" + str(pageTable[arrayNum]["id"])
		print sourceURL
		urllib.urlretrieve(imageURL, 'image.jpg')
		
		# Fill the empty string with the hashtags you want.
		tweetString = sourceURL + " "
		api.update_with_media('image.jpg', status=tweetString)
		
		os.remove('image.jpg')
		# You can replace the number with however often you want to post. Limited to 500 requests/hour.
		time.sleep(1800)
		
	except tweepy.error.TweepError:
		print "Image too large, finding a different image..."
