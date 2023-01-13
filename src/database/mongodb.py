import pymongo
import os


import certifi
ca = certifi.where()


class MongodbOperation:

    def __init__(self) -> None:
        mongo_url = os.environ("MONGO_URL")
        self.client = pymongo.MongoClient(mongo_url, tlsCAFile=ca)
        self.db_name = os.environ("DATABASE")
        self.coll_name = os.environ("COLLECTION")

    def insert_many(self, collection_name, records: list):
        self.client[self.db_name][self.coll_name].insert_many(records)

    def insert(self, collection_name, record):
        self.client[self.db_name][self.coll_name].insert_one(record)
