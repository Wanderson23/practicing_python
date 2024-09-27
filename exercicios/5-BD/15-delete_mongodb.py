from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

#Deletendo valores

myquery = {"title": "FastApi"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documento(s) excluido(s)")

