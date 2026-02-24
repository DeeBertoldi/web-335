"""
Title: Bertoldi_usersp1.py
Author: Daniella Bertoldi
Date: 23 February 2026
Description: Exercise 6.3 - Python with MongoDB, Part I
"""

from pymongo import MongoClient

# connect to mongo
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Accessing web335DB database
db = client['web335DB']

# Display all users 
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

# Display a document where employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# Display a document where lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))