import json
from bson.objectid import ObjectId
from pymongo import MongoClient
import os

client = MongoClient("mongodb+srv://web_10MHW:H5PUL8zRh2SEThAH@hedgehog.rsn29se.mongodb.net/hw?retryWrites=true&w=majority&appName=hedgehog")
# client = MongoClient("mongodb://localhost:27017/")
db = client.hw

# Виведення усіх файлів у поточному каталозі
print("Файли у поточному каталозі:")
for filename in os.listdir('.'):
    if os.path.isfile(filename):
        print(filename)

# Перевірка наявності файлу quotes.json
if os.path.isfile('quotes.json'):
    with open('quotes.json', encoding='utf-8') as f:
        quotes = json.load(f)
    print("Зміст файлу quotes.json:")
    print(quotes)

    for quote in quotes:
        author = db.authors.find_one({"fullname": quote["author"]})
        if author:
            inserted_quote = {
                "quote": quote["quote"],
                "tags": quote["tags"],
                "author": ObjectId(author["_id"]),
            }
            db.quotes.insert_one(inserted_quote)
            print("Додано до бази: ", inserted_quote)
    print("Дані успішно записано до бази.")
else:
    print("Файл quotes.json не знайдено.")