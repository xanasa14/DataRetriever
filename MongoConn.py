
import pymongo
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")
# Database Name
db = client["HistoricalPlaces"]

# Collection Name
col = db["celebrities"]



