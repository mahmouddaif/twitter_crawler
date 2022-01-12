# twitter_crawler
# TwitterCrawler
## Installation 
```
pip install -r requirements.txt
```
## Usage
```
python TendExtractor.py
```
This is a cron job that will run in the background and update the trends once every 8 hours.

```
python Crawler.py
```
This is the twitter crawler.

## Configs

```
[Main]
ckey=xxxxxxxxxxxxxxxxxxxxxxx
csecret=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
atoken=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
asecret=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
out_folder=./output/
sleep_interval=1
continous_tweet_limit=1000
```
**ckey**, **csecret**, **atoken**, **asecret**: Twitter API credentials.  
**out_folder**: Output folder.  
**sleep_interval**: number of seconds the crawler sleeps after a certain number of tweets is crawled!  
**continous_tweet_limit**: number of tweets to crawl before sleeping for a specified number of seconds!

