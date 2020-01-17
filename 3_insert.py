import datetime
from base import db, collection
from pprint import pprint
from bson.objectid import ObjectId

# 插入
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}
# 返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值
result = collection.insert_one(post)
post_id = result.inserted_id
print("post id is ", post_id)
print(type(ObjectId(post_id)))


# 列出数据库中的所有集合
cur_collection = db.list_collection_names()
print("cur_collection is :", cur_collection)  # cur_collection is : ['jdq', 'system.indexes']
