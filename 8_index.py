from base import db, collection
import pymongo

collection.create_index([("user_id", pymongo.ASCENDING)], unique=True)
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
sorted(list(collection.index_information()))

# user_profiles = [{'user_id': 211, 'name': 'Luke'}, {'user_id': 212, 'name': 'Ziltoid'}]
# result1 = collection.insert_many(user_profiles)
#
# new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# result2 = collection.insert_one(new_profile)  # This is fine.

# user_id 现在是索引且唯一, 所以添加不上
result3 = collection.insert_one(duplicate_profile)
