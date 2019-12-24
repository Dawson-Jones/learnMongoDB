from base import collection


"""
Data:

{
   _id: ObjectId(7df78ad8902c)
   title: 'MongoDB Overview', 
   description: 'MongoDB is no sql database',
   by_user: 'runoob.com',
   url: 'http://www.runoob.com',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 100
},
{
   _id: ObjectId(7df78ad8902d)
   title: 'NoSQL Overview', 
   description: 'No sql database is very fast',
   by_user: 'runoob.com',
   url: 'http://www.runoob.com',
   tags: ['mongodb', 'database', 'NoSQL'],
   likes: 10
},
{
   _id: ObjectId(7df78ad8902e)
   title: 'Neo4j Overview', 
   description: 'Neo4j is no sql database',
   by_user: 'Neo4j',
   url: 'http://www.neo4j.com',
   tags: ['neo4j', 'database', 'NoSQL'],
   likes: 750
}
"""

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

# result: [{'_id': 'runoob.com', 'num': 2}, {'_id': 'Neo4j', 'num': 1}]
# 类似于 select by_user, count(*) from gdb group by by_user

print(list(res))
