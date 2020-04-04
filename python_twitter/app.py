# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
import json
import re


#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'd5iIixj52ix2CHuVGLjpqzbsI' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'MCn9wSfO0f6PLZsgBBggnU8m6GMdNfAxkN01XAGibFGMzJd0Nu' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '998590173687447557-uXJsuRCbOvdeQWytBEkYxynqrpKZYXz' #keep the quotes, replace this with your access token
ACCESS_SECRET = 'peWod2S54FzZbF90JSLRi9yWv2ULiSLYIi4BycxqMNJsy' #keep the quotes, replace this with your access token secret


# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

tweets = api.search('#comesquarentenafaigunbot')

print(tweets)
