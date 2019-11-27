import datetime
from base import db, collection
from pprint import pprint

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

# 批量插入
new_posts = [
    {"_id": 1000,
     "author": "Curry",
     "text": "Another post!",
     "tags": ["bulk", "insert"],
     "date": datetime.datetime(2017, 11, 12, 11, 14)},
    {"_id": 1001, "author": "Maxsu",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime(2019, 11, 10, 10, 45)}
]
result = collection.insert_many(new_posts)
print("Bulk Inserts Result is :", result.inserted_ids)  # Bulk Inserts Result is : [1000, 1001]


# 列出数据库中的所有集合
cur_collection = db.list_collection_names()
print("cur_collection is :", cur_collection)  # cur_collection is : ['jdq', 'system.indexes']
