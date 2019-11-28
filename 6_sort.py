import pprint
from base import db, collection

# sort() 方法第一个参数为要排序的字段，第二个参数指定排序规则，1 为升序，-1 为降序，默认为升序。
my_doc = collection.find({}, {"_id": 0}).sort("name", -1)
for i in my_doc:
    pprint.pprint(i)
