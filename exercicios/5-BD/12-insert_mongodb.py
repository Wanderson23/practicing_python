from pymongo import MongoClient

client = MongoClient()

print(client)
mydb = client.obcblog
mycol = mydb.posts

post1 = {
    "title": "FastApi",
    "category": "BackEnd",
    "author": {
        "name": "Rodrigo",
        "email": "Rodrigo@email.com"
    }
}

result = mycol.insert_one(post1)
print("Documento incluido com sucesso")