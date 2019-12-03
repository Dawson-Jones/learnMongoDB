import pprint
from base import db, collection


# update_one() 方法只能修匹配到的第一条记录 必须用$符号
# 将作者 Maxsu 改为 Mike
collection.update_one({"author": "Maxsu"}, {"$set": {"author": "Mike"}})
for i in collection.find():
    pprint.pprint(i)

# replace_one() 代替
q_res = collection.find_one({'name': 'jdq'})
print(q_res)
res = collection.replace_one(q_res, {"name": 'dobby', 'age': 18})
print(res.upserted_id)
print(res.raw_result)

# 修改所有匹配到的记录，使用 update_many()
# 查找所有以 F 开头的 name 字段，并将匹配到所有记录的 alexa 字段修改为 123
myquery = {"name": {"$regex": "^F"}}
newvalues = {"$set": {"alexa": "123"}}

x = collection.update_many(myquery, newvalues)
print(x.modified_count, "文档已修改")  # 0 文档已修改
