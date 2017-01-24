import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname': 'Marek', 'lastname': 'Rewers'}
print doc
print "about to insert the document"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e

print doc
print "inserting again"

try:
    users.insert_one(doc)
except Exception as e:
    print "insert failed:", e
