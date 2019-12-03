from base import collection

res = collection.aggregate([
    {'$group':
        {
            '_id': '$by_user',
            'num': {'$sum': 1}
        }
    },
    {'$sort': {'num': -1}},
    {'$limit': 2},
])

print(list(res))
