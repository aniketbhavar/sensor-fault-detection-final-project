import pymongo
from urllib.parse import quote_plus
from sensor.constant.database import DATABASE_NAME
#from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                username = "aniket"
                password = "Aniket@1234"
                cluster_url = "cluster0.djqdoeg.mongodb.net"
                mongo_db_url= f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}@{cluster_url}/?retryWrites=true&w=majority"
                #mongo_db_url = "mongodb+srv://aniket:Aniket@1234@cluster0.djqdoeg.mongodb.net/?retryWrites=true&w=majority"
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e