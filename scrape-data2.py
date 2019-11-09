import tweepy
import codecs
import my_keys
import json

# Get the authentication keys from my_keys.py
CONSUMER_KEY = my_keys.CONSUMER_KEY
CONSUMER_SECRET = my_keys.CONSUMER_SECRET
ACCESS_KEY = my_keys.ACCESS_KEY
ACCESS_SECRET = my_keys.ACCESS_SECRET

# Authenticate to Twitter with our keys
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth1)

class StreamListener(tweepy.StreamListener):
 #   def on_data(self, data):
        #data = json.loads(data)
        #print(data['extended_tweet']['full_text'])
        #tweet = data.text
        #print(data)
        #all_data = json.loads(data)

        #all_data = json.loads(data)

        #tweet = all_data["text"]
        
        #print(tweet)

  #      for row in data:
  #          print(row[0])
            
   #     if not ('RT @' in data) :	
   #          print("\"%s\"" % (data))

   #      if not ('RT @' in row) :	
   #          #print("\"%s\"" % (row['text']))
   #          print(row)
        
    def on_status(self, status):
        #all_data = json.loads(status)
        #tweet = all_data['text']

        
        #tweet = status._json
        #tweet = status.text


        #if status.lang == 'en' and 'RT'.upper() not in status.text :
        if status.lang == 'en':
            stat = status.text
        #stat = stat.replace('\n','')
        #stat = stat.replace('\t','')
            stat = stat.replace('.....','')
            stat = stat.replace('....','')
            stat = stat.replace('...','')
            stat = stat.replace('..','')
            stat = stat.replace('…','')
            stat = stat.replace('…','')  
            tweet =stat
                              
 #       tweet = status.text
        #truncated = true
 #       tweet_mode = 'extended'
 #       count=2
        #user = status.author
        #userid = status.author.id
        #time = status.created_at
        #source = status.source
        #tweetid = status.id

 #       print("\"%s\"" % (text))

    #    print("STATUS: " + status.text)

        if not ('RT @' in tweet) :	
            print("\"%s\"" % (tweet))
            #print("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"" % (tweet,user,userid,time,source))

StreamListener = StreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=StreamListener)
            
#myStream.filter(track=['python'])

#myStream.filter(track=['slowdown','cost of living','expensive'])
myStream.filter(track=['economic slowdown','expensive','cost of living'])

#'cost of living',’expensive’,’slowdown’

