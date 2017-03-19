import pymongo
import pandas as pd

class Mongo_Grabber:

    def __init__(self, username, password, server, port):
        self.username = username
        self.password = password
        self.server = server
        self.port = port

    def get_data(self, database):
        db = self.mongo_authenticated(database)
        return pd.DataFrame(list(db.http_bank.find()))


    def mongo_authenticated(self, database):
        mongo_connection = pymongo.MongoClient('mongodb://'+self.username+':'+self.password+'@'+self.server+':'+self.port+'/')
        db = mongo_connection[database]
        return db
