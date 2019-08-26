from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)
db = client.test_db
collection = db.test_collection
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

doc = db.test_doc
doc_id = doc.insert_one(post).inserted_id
doc_id
