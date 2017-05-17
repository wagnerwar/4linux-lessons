from pymongo import MongoClient
client = MongoClient('127.0.0.1')
db = client['devops']

print(db)
"""
# Realizando uma insercao
db.fila.insert({"_id": 3,"servico" : "Internet", "status":0})
db.fila.insert({"_id": 4,"servico" : "Intranet", "status":1})
"""

# Realizando uma atualizacao

db.fila.update({"_id":1},{"$set":{"servico":"Pedreiro"}})


