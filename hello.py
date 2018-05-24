import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['blog_app']
collection = database['users']

collection.remove({})

collection.insert({"name": "bobross", "pass": "bob"})

users = collection.find({})
for user in users:
    print(user)
