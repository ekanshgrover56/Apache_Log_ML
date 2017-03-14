import pymongo
import pandas as pd

class Mongo_Grabber:

    def __init__(self, dictionary, username, password, server, port):
        self.dictionary = dictionary
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        #self.mongo_connector = pymongo.MongoClient('mongodb://'+username+':'+password+'@'+server+':'+port)
        #self.mongo_connection = self.mongo_connector.http_bank
        #print(self.mongo_connector)
        #print(self.mongo_connection)
        #self.mongo_connection = mongo_connector.http_bank

    def get_data(self, command, database):
        db = self.mongo_authenticated(database)
        #return db.http_bank.aggregate(command)
        return pd.DataFrame(list(db.http_bank.find()))


    def mongo_authenticated(self, database):
        mongo_connection = pymongo.MongoClient('mongodb://'+self.username+':'+self.password+'@'+self.server+':'+self.port+'/')
        db = mongo_connection[database]
        return db
