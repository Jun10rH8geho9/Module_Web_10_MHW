import json
from bson import ObjectId
from pymongo import MongoClient

# client = MongoClient("mongodb+srv://web_10MHW:YAtH9nYxSnwoLQiU@hedgehog.rsn29se.mongodb.net/web_10_django?retryWrites=true&w=majority&appName=hedgehog")
client = MongoClient("mongodb://localhost:27017/")
db = client.web_10_django

with open("quotes.json", "r", encoding="utf-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({"fullname": quote["author"]})
    if author:
        db.quotes.insert_one({
            "author": ObjectId(author["_id"]),
            "quote": quote["quote"],
            "tags": quote["tags"],
        })