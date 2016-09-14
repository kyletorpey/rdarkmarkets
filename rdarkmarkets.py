import praw
import time
import tweepy
 
CONSUMER_KEY = '************'
CONSUMER_SECRET = '************'
ACCESS_TOKEN = '************'
ACCESS_TOKEN_SECRET = '************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

r = praw.Reddit(user_agent = "Twitter:@rdarkmarkets:v0.1 by /u/kyletorpey")

launchtime = time.time()
cache = []

def run_bot():
	subreddit = r.get_subreddit("darknetmarkets")
	posts = subreddit.get_hot(limit=10)

	for post in posts:
		post_url = post.url
		post_title = post.title
		post_title = post_title[:115]
		post_votes = post.score
		tweet = post_title + " " + post_url
		
		if (post.id not in cache) and (post_votes > 14) and (post.created_utc > launchtime):
			api.update_status(tweet)
			print (time.strftime("%m/%d/%Y")) + " " + (time.strftime("%H:%M:%S")) + " Tweet sent: " + tweet
			cache.append(post.id)
		else:
			print "No new posts."

while True:
	run_bot()
	time.sleep(300)

###TO DO LIST###
#remove stuff from cache if it's a month old
