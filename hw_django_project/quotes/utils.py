from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://web_10MHW:H5PUL8zRh2SEThAH@hedgehog.rsn29se.mongodb.net/hw?retryWrites=true&w=majority&appName=hedgehog")
    db = client.hw
    return db