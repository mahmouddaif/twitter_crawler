#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from CSVManager import CSVManager
import re
from urllib3.exceptions import ProtocolError
from Utils import read_words_list
from time import sleep
from datetime import datetime
import time
from ConfigParser import ConfigsLoader


class listener(StreamListener):
    def __init__(self, out_folder):
        super().__init__()
        self.out_folder = out_folder
        self.csv_manager = CSVManager(self.out_folder)
        self.tweets_per_file = 100000
        self.current_tweet = 0
        self.header = ["created_at",
                       "id",
                       "source",
                       "text",
                       "screen_name",
                       "coordinates.long",
                       "coordinates.lat",
                       "place.country_code",
                       "place.name",
                       "place.place_type",
                       "place.log1",
                       "place.lat1",
                       "place.log2",
                       "place.lat2",
                       "place.log3",
                       "place.lat3",
                       "place.log4",
                       "place.lat4",
                       "hash_tags",
                       "urls",
                       "user_mentions",
                       "symbols"]
        current_datetime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        self.current_file = self.out_folder + current_datetime+"_tweet.csv"
        self.csv_manager.write_list_to_file(self.header,self.current_file)
        self.current_tweet = 0
        

    def on_data(self, data):
        all_data = json.loads(data)
        
        #print(all_data)
        if "created_at" not in all_data:
            print("Limit reached, sleeping! " +  datetime.now().strftime("%d_%m_%Y_%H_%M_%S"))
            sleep(1)
            return True
        
        hashtags = all_data["entities"]["hashtags"]
        
        urls = all_data["entities"]["urls"]
        
        user_mentions = all_data["entities"]["user_mentions"]
        
        symbols = all_data["entities"]["symbols"]
        
        created_at = all_data["created_at"]
        
        tweet_id = all_data["id_str"]
        
        source = all_data["source"]


        tweet = all_data["text"].strip().replace('\n', ' ').replace('\r', '').replace(","," ")
        tweet = re.sub("\s\s+", " ", tweet)


        username = all_data["user"]["screen_name"]
        
        
        coordinates_long = "None"
        coordinates_lat = "None"

        if all_data['coordinates'] is not None:
            coordinates_long = str(all_data['coordinates']["coordinates"][0])
            coordinates_lat = str(all_data['coordinates']["coordinates"][1] )
        
        place_country_code = "None"
        place_name = "None"
        place_place_type = "None"
        place_log1 = "None"
        place_lat1 = "None"
        place_log2 = "None"
        place_lat2 = "None"
        place_log3 = "None"
        place_lat3 = "None"
        place_log4 = "None"
        place_lat4 = "None"

        
        if all_data['place'] is not None:
            place_country_code = all_data['place']["country_code"]
            place_name = all_data['place']["name"]
            place_place_type = all_data['place']["place_type"]
            print(all_data['place'])
            place_log1 = str(all_data['place']["bounding_box"]["coordinates"][0][0][0])
            place_lat1 = str(all_data['place']["bounding_box"]["coordinates"][0][0][1])
            place_log2 = str(all_data['place']["bounding_box"]["coordinates"][0][1][0])
            place_lat2 = str(all_data['place']["bounding_box"]["coordinates"][0][1][1])
            place_log3 = str(all_data['place']["bounding_box"]["coordinates"][0][2][0])
            place_lat3 = str(all_data['place']["bounding_box"]["coordinates"][0][2][1])
            place_log4 = str(all_data['place']["bounding_box"]["coordinates"][0][3][0])
            place_lat4 = str(all_data['place']["bounding_box"]["coordinates"][0][3][1])
            
        tweet_list = [
            created_at,
            tweet_id,
            source,
            tweet,
            username,
            coordinates_long,
            coordinates_lat,
            place_country_code,
            place_name,
            place_place_type,
            place_log1,
            place_lat1,
            place_log2,
            place_lat2,
            place_log3,
            place_lat3,
            place_log4,
            place_lat4,
            json.dumps(hashtags).replace(",","-"),
            json.dumps(urls).replace(",","-"),
            json.dumps(user_mentions).replace(",","-"),
            json.dumps(symbols).replace(",","-")
            ]
        #print("h: ",len(self.header))
        #print("l: ", len(tweet_list))

        self.current_tweet +=1
        self.csv_manager.write_list_to_file(tweet_list,self.current_file)
        if self.current_tweet%self.tweets_per_file == 0:
            self.current_tweet = 0

            current_datetime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            self.current_file = self.out_folder + current_datetime+"_tweet.csv"
            self.csv_manager.write_list_to_file(self.header,self.current_file)



        #print(all_data)

        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    configFileName = "Configs.ini"
    configLoader = ConfigsLoader(configFileName)
    
    configs = configLoader.get_configs()
    ckey = configs.get("Main","ckey")
    csecret = configs.get("Main","csecret")
    atoken = configs.get("Main","atoken")
    asecret = configs.get("Main","asecret")
    out_folder = configs.get("Main","out_folder")

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener(out_folder))
    words_list = read_words_list("words_list.txt")
    running = datetime.now()

    while True:
        try:
            now = datetime.now()
            if twitterStream.running is True and (now.minute - running.minute) == 8: 
                print("already been 8 minutes")
                running = datetime.now()
                twitterStream.disconnect()
                words_list = read_words_list("words_list.txt")
                twitterStream.filter(languages=['ja'], track=words_list, is_async=True)
            elif twitterStream.running is False : 
                print("not runnning")
                running = datetime.now()
                twitterStream.filter(languages=['ja'], track=words_list, is_async=True)
                time.sleep(3600)
                
            
        except (ProtocolError, AttributeError):
            continue
