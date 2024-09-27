from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

#Alterando valor de um campo 
old_value = {"category": "Data"}
new_value = {"$set":{"category": "Backend"}}

mycol.update_one(old_value, new_value)

for r in mycol.find():
    print(r)