import pymongo
from pymongo import MongoClient

ds = MongoClient("mongodb+srv://akhilabhi:akhilabhi@cluster0.pr7mtdr.mongodb.net/?retryWrites=true&w=majority")
db = ds["bot"]
