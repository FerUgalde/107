import pymongo
import certifi

con_str = "mongodb+srv://FSDI:test123@107.1agwdeb.mongodb.net/?retryWrites=true&w=majority&appName=107"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("107test2")