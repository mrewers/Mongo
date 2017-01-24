import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
grades = db.grades

def dropScore():

    try:
        cursor = grades.find({'type': 'homework'}).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    previous_id = None
    student_id = None

    for doc in cursor:
        student_id = doc['student_id']
        if student_id != previous_id:
            previous_id = student_id
            print "Removing", doc
            grades.remove( { '_id': doc[ '_id'] } )

dropScore()
