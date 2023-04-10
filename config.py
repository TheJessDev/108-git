import pymongo
import certifi


con_str = "mongodb+srv://1jlmorrison:test1234@cluster0.yf71o9b.mongodb.net/?retryWrites=true&w=majority"

# change password with no brackets around password! 

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore")

# db variable is databse 

