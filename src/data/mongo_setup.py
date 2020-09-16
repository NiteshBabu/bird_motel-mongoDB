from mongoengine import connect
import os, pprint

from keys import host 
# import pymongo
# client = pymongo.MongoClient("mongodb://self:nitesh123@cluster0-shard-00-00.63hur.mongodb.net:27017,cluster0-shard-00-01.63hur.mongodb.net:27017,cluster0-shard-00-02.63hur.mongodb.net:27017/sample_mflix?ssl=true&replicaSet=atlas-s2h4ty-shard-0&authSource=admin&retryWrites=true&w=majority")

# alias_core = 'core'
# db = 'Bird_Motel'
# data = dict( 
#   username = 'self', 
#   password = 'nitesh123', 
#   host = 'cluster0-shard-00-00.63hur.mongodb.net',
#   port = '27017', 
#   authentication_source = 'admin',
#   authentication_mechanism = 'SCRAM-SHA-1', 
#   ssl = 'True', 
#   ssl_cert_reqs = 'ssl.CERT_NONE'  
# )

def global_init():
  # client = mongoengine.register_connection(alias=alias_core, name=db, **data)
  client = connect(host = host)

