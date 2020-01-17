"""
MongoDB中执行的最基本的查询类型是find_one()。
此方法返回与查询匹配的单个文档(如果没有匹配，则返回None)。
当知道只有一个匹配的文档，或只对第一个匹配感兴趣时则可考虑使用find_one()方法。
"""
import pprint
import datetime
from base import collection
from bson.objectid import ObjectId

# 单个查询
# pprint.pprint(collection.find_one())
# 指定查询的条件, 查询作者是“Maxsu”的文档
pprint.pprint(collection.find_one({'description': 'MongoDB is no sql database'}, {'by_user': 1}))


# 多个查询
print('#' * 40)
print(list(collection.find()))
print('#' * 40)
print(collection.find())
for i in collection.find():  # 遍历所有查询 -> select *
    pprint.pprint(i)
print('*' * 40)
for i in collection.find({"author": "Maxsu"}):  # 过滤条件
    pprint.pprint(i)
print('*' * 40)
# 查询指定字段的数据，将要返回的字段对应值设置为 1
for i in collection.find({}, {"_id": 0, "name": 1, "author": 1}):
    pprint.pprint(i)
# 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
print('*' * 40)

# 高级查询
# 读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"}, 不要 _id 字段
for i in collection.find({"name": {"$gt": "H"}}, {"_id": 0}):
    pprint.pprint(i)
print('-' * 40)
# 使用正则表达式查询
for i in collection.find({"name": {"$regex": "^j"}}, {"_id": 0}):
    pprint.pprint(i)
print('*' * 40)

# 查询键 by 值为 菜鸟教程 或键 title 值为 MongoDB 教程 的文档
collection.find({
    '$or': [
        {'by': '菜鸟教程'},
        {'title': 'MongoDB教程'}
    ]
})

# AND 和 OR 联合使用
""" where likes>50 AND (by = '菜鸟教程' OR title = 'MongoDB 教程') """

collection.find({
    "likes": {'$gt': 50},
    '$or': [
        {'by': '菜鸟教程'},
        {'title': 'MongoDB教程'}
    ]
})


# 查询到的数量
# print("posts's author is Maxsu count is =", collection.find({"author": "Maxsu"}).count())  # 被下面的替代
print("posts's author is Maxsu count is =", collection.count_documents({"author": "Maxsu"}))


# 返回指定条数记录
print("返回3条数据")
for i in collection.find().limit(3):
    pprint.pprint(i)
print('*' * 40)

# 范围查询
d = datetime.datetime(2019, 11, 12, 12)
for post in collection.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)


# 通过ObjectId查询
"""
Web应用程序中的常见任务是从请求URL获取ObjectId并找到匹配的文档。 在这种情况下，必须将ObjectId从一个字符串转换到find_one()
"""
# from bson.objectid import ObjectId
# # The web framework gets post_id from the URL and passes it as a string
# def get(post_id):
#     # Convert from string to ObjectId:
#     document = collection.find_one({'_id': ObjectId(post_id)})
