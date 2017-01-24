import pymongo
from pymongo import MongoClient

#connection to Database
connection = MongoClient('localhost', 27017)

db = connection.test

#handle to names collection
names = db.names

item = names.find_one()

print item['name']
