"""
Title: bertoldi_usersp2.py
Author: Daniella Bertoldi
Date: 01 March 2026
Description: Exercise 7.3 - Python with MongoDB, Part II
"""

# ============================================================
#
# remembering "formula" and template structure for reference :CRUD:
# CONNECT
# CREATE
# PROVE
# UPDATE
# PROVE
# DELETE
# PROVE
#
# STRUCTURE TEMPLATE:
# 1. Header comment
# 2. Import libraries
# 3. Create connection
# 4. Select database
# 5. Perform operation
# 6. Print proof
#
# Everything revolves around:
# db.collection.method(filter, operation)
# ============================================================

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Configure a variable to access the web335DB
db = client['web335DB']

# ----------------------------
# CREATE A NEW USER DOCUMENT
# ----------------------------

new_user = {
    "firstName": "Daniella",
    "lastName": "Dreamer",
    "employeeId": "1014",
    "email": "ddreamer@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into collection
new_user_id = db.users.insert_one(new_user).inserted_id

# Print document ID
print(new_user_id)

# ----------------------------
# PROVE THE DOCUMENT WAS CREATED

print(db.users.find_one({"employeeId": "1014"}))


# ----------------------------
# UPDATE THE USER EMAIL

db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "daniella.dreamer@me.com"
        }
    }
)

# ----------------------------
# PROVE THE DOCUMENT WAS UPDATED


print(db.users.find_one({"employeeId": "1014"}))

# ----------------------------
# DELETE THE USER DOCUMENT

result = db.users.delete_one({"employeeId": "1014"})

print(result.deleted_count)

# ----------------------------
# PROVE THE DOCUMENT WAS DELETED

print(db.users.find_one({"employeeId": "1014"}))