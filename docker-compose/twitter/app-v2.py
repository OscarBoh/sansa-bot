# tweepy will allow us to communicate with Twitter, time will allow us to set how often we tweet
import tweepy, time
import json
import re


#enter the corresponding information from your Twitter application management:
CONSUMER_KEY = 'd5iIixj52ix2CHuVGLjpqzbsI' #keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'MCn9wSfO0f6PLZsgBBggnU8m6GMdNfAxkN01XAGibFGMzJd0Nu' #keep the quotes, replace this with your consumer secret key
ACCESS_TOKEN = '998590173687447557-uXJsuRCbOvdeQWytBEkYxynqrpKZYXz' #keep the quotes, replace this with your access token
ACCESS_SECRET = 'peWod2S54FzZbF90JSLRi9yWv2ULiSLYIi4BycxqMNJsy' #keep the quotes, replace this with your access token secret

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        print(status.id)
        print(status.id_str)
                
    def on_error(self, status):
        print(status)
        return True

    def on_data(self, data):
        data_j=json.loads(data)
        #print(data_j)
        if 'retweeted_status' in data_j:
          print('it is a retweet')
        else:
          api.retweet(data_j['id'])

# configure our access information for reaching Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

tweets = api.search('#comesquarentenafaigunbot')
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['#comhihaquarentenafaigunbot'])


