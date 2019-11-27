import datetime
from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['test']
collection = db['jdq']

db_list = client.list_database_names()
print(f'db_list: {db_list}')

collection_list = db.list_collection_names()
print(f'collection_list: {collection_list}')

# collection.find_one({'_id': 100})
# print(collection.count_documents({'author': 'Maxsu'}))
# collection.find(1)
x = collection.delete_many({'author': {'$regex': '^.'}})
for doc in collection.find():
    pprint(doc)
print(f'delete {x.deleted_count} documents')
