from pymongo import MongoClient

# MongoDB的客户端
# client = MongoClient("mongodb://root:123456@localhost:27017,localhost:28018,localhost:29019")
client = MongoClient("localhost", 27017)
# MongoDB database
db = client['test']
# collection 相当于 table
collection = db['gdb']
