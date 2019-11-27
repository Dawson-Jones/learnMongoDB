import pprint
from base import db, collection

# 删除一个文档
collection.delete_one({"name": "sb"})

for i in collection.find():
    pprint.pprint(i)

# 删除多个文档, 删除所有 name 字段中以 F 开头的文档
x = collection.delete_many({"name": {"$regex": "^F"}})
print(x.deleted_count, '个文档已经删除')

# 删除集合中的所有文档  delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档
x = collection.delete_many()
print(x.deleted_count, '个文档已经删除')  # 5 个文档已删除

# # 删除集合 使用 drop() 方法来删除一个集合
# collection.drop()
# # 删除成功 drop() 返回 true，如果删除失败(集合不存在)则返回 false
