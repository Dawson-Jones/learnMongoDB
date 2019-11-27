from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient('localhost', 27017)
# MongoDB database
db = client['test']
# collection 相当于 table
collection = db['jdq']
