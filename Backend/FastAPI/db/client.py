from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient(
    "mongodb+srv://ramiandino:gaseq123456@cluster0.ahnveq4.mongodb.net/?retryWrites=true&w=majority"
)
