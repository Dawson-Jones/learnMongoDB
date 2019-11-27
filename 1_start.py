import datetime
from pymongo import MongoClient
from pprint import pprint

# mongoDB的客户端
client = MongoClient('localhost', 27017)
# mongoDB database
db = client['test']
# collection 相当于 table
collection = db['jdq']

# post = {
#         "author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()
# }

new_posts = [{"_id": 1000,
              "author": "Curry",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2017, 11, 12, 11, 14)},
             {"_id": 1001,
              "author": "Maxsu",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2019, 11, 10, 10, 45)}]

# post_id = collection.insert_one(post).inserted_id
result = collection.insert_many(new_posts)

# print('post id is: ', post_id)
print('post id is: ', result.inserted_ids)
collection.find_one()
