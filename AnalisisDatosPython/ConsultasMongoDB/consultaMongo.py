#!/bin/usr/env python3
import pymongo
from pymongo.errors import ServerSelectionTimeoutError
#from pymongo import MongoClient

MONGO_USERNAME="sym_admin"
MONGO_PASSWORD="QkZEp4sQrAeJTZMu"
MONGO_URI=f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@mongo-izzi-prod-shard-00-00.ytutu.mongodb.net:27017,mongo-izzi-prod-shard-00-01.ytutu.mongodb.net:27017,mongo-izzi-prod-shard-00-00.ytutu.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-1srns6-shard-0&authSource=admin&retryWrites=true&w=majority"
cliente = MongoClient(f"{MONGO_URI}")
MONGO_AUTH_DB="admin"
print(MONGO_URI.list_database_names())

MONGO_HOST = 'mongo-izzi-prod-shard-00-00.ytutu.mongodb.net'
MONGO_PORT = 27017
MONGO_USERNAME="sym_admin"
MONGO_PASSWORD="QkZEp4sQrAeJTZMu"
MONGO_TIMEOUT = 1000
#MONGO_URI="mongodb://sym_admin:QkZEp4sQrAeJTZMu@mongo-izzi-prod-shard-00-00.ytutu.mongodb.net:27017,mongo-izzi-prod-shard-00-01.ytutu.mongodb.net:27017,mongo-izzi-prod-shard-00-00.ytutu.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-1srns6-shard-0&authSource=admin&retryWrites=true&w=majority"
MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"

try:
    cliente = pymongo.MongoClient(MONGO_URI,ServerSelectionTimeoutMS=MONGO_TIMEOUT)
    cliente.server_info()
    print("Conexiń a mongo exitosa")
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo en conectarse a MongoDB")

#def conectar_db():
#    host = 'localhost'
#    puerto  = 35713
#    usuario = 'sym_admin'
#    password = 'QkZEp4sQrAeJTZMu'
#    db = 'sym-inventory-manager'
#    cliente = MongoClient(f"mongodb://{usuario}:{password}@{host}:{puerto}/")
#    return cliente[db]
#
#def consultar():
#    bd = conectar_db()
#    for i in bd.services.find():
#        print(i)

#print(consultar())
#
#colección
#Inventario Servicios


