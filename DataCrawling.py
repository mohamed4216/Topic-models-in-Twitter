#!/usr/bin/python
import tweepy
import time
# Authenticate Tweet API
auth = tweepy.AppAuthHandler('Jipy5FT9mnuBhaL3tx6cwaraD', '4UUNPGllQGExdnqDx5giE5Qzgz8UPhRAuAHaRr1RSGkY9crNAD')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Open/Create a file to append data
output = open('rawData.txt', 'a')

# Collect tweets
Tweets = tweepy.Cursor(api.search, q="europe german", lang="en").items()
while True:
    try:
	tweet = Tweets.next()
	if (not tweet.retweeted) and ('RT @' not in tweet.text):
    		#Write  to the Output
    		output.write(tweet.text.encode('utf-8')+"\n")
    		print tweet.created_at, tweet.text
    except tweepy.TweepError:
       	time.sleep(60*15)
        continue

#close Output
output.close()

   
