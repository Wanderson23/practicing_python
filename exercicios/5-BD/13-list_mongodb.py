from pymongo import MongoClient
from pprint import pprint #Para trazer formatado as linhas , uma embaixo da outra

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

#Retorna um documento
#result = mycol.find_one()

#Retorna todos os documentos
result = mycol.find()

for r in result:
    pprint(r)