import json
import urllib2
import pymongo

connection=p

db=connection.reddit
stories=db.stories

stories.drop()

reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

for item in parsed['data']['children']
