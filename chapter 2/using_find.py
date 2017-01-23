import pymongo
import sys

# establish a connection to the datbase
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores

def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}

    try:
        doc = scores.find_one(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    print doc

def find():

    print "find, reporting for duty"
    query = {'type':'exam'}

    try:
        cursor = scores.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if (sanity > 10):
            break

find()