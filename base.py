from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient("mongodb://root:123456@localhost:27017,localhost:28018,localhost:29019")
# MongoDB database
db = client['dobby_db']
# collection 相当于 table
collection = db['dobby_cc']
