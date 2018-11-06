


import pymongo

# 获取连接mongodb的对象
client = pymongo.MongoClient("127.0.0.1",port=27017)

# 获取数据库（如果没有zhihu数据库，也可以）
# db = client.wade
db = client['admin']
db.authenticate('sa', 'sa')

# 获取数据库中的表（qa也可以不存在）
collection = db.qa

# 写入数据
# collection.insert({"username":"靓仔"})


collection.insert_many([
    {
        "username":"aaa",
        "age":20
    },
    {
        "username":"aaa",
        "age":19
    }
])

# 查找数据
# cursor = collection.find()
# for x in cursor:
#     print(x)

# 2、获取集合中一条数据
# result = collection.find_one({"age":18})
# print(result)


# 更新数据
# collection.update_one({"username":"aaa"},{"$set":{"username":"ccc"}})

# 更新过个，把所有aaa的都改成hhh
# collection.update_many({"username":"aaa"},{"$set":{"username":"hhh"}})

# 删除数据
# collection.delete_one({"username":"Kobe"})

collection.delete_many({"username":"aaa"})

