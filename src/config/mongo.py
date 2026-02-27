from pymongo import MongoClient
import os

def collections(name):
    username = os.getenv('MONGO_USERNAME')
    password = os.getenv('MONGO_PASSWORD')
    host = os.getenv('MONGO_HOST')
    port = os.getenv('MONGO_PORT')
    url = f'mongodb://{username}:{password}@{host}:{port}/'
    client = MongoClient(url)
    return client['todo'][name]