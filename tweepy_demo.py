#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from datetime import datetime



#consumer key, consumer secret, access token, access secret.
ckey="xxlzzY0tph2dY5YHQcyDt0EsE"
csecret="GTd05ExHrkmfvJz7zjqfI6OFhzhOTbJ3wMA4VmfIpxdy3hlwAX"
atoken="185665986-db7p8ss7eAEZrT32bHqBIzi8ssfD8bRkoAm6t9PL"
asecret="MCkxkHkjQ9wDroubx2CrJr1nL1wPQFZf4o3mD26J9MM34"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]
        
        created_at = all_data["created_at"]
        
        

        if all_data['coordinates'] is not None:
            print(all_data['coordinates'])



        #print(all_data)

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(languages=['ja'], track=['あ','い','え','う','お'])


