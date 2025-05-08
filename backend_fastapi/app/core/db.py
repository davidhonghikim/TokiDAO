from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import ConnectionFailure
from app.core.config import settings
from typing import Optional

class MongoDBConnection:
    client: Optional[MongoClient] = None
    db: Optional[Database] = None

    async def connect_to_mongo(self):
        if not settings.MONGODB_URI:
            print("MONGODB_URI not set in environment variables. Cannot connect to MongoDB.")
            return
        print(f"Attempting to connect to MongoDB at: {settings.MONGODB_URI[:20]}...")
        try:
            self.client = MongoClient(settings.MONGODB_URI, serverSelectionTimeoutMS=5000)
            # The database name can be part of the MONGODB_URI or specified here.
            # If your MONGODB_URI includes the database name, like:
            # mongodb+srv://user:pass@cluster/myDatabase?retryWrites=true&w=majority
            # then self.client.get_database() will use 'myDatabase'.
            # Otherwise, you can specify it: self.db = self.client.get_database("tokidao_db")
            self.db = self.client.get_database() # Assumes DB name is in URI or uses default 'test'
            
            # Verify connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB.")
            print(f"Using database: {self.db.name}")
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")
            self.client = None
            self.db = None

    async def close_mongo_connection(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

    def get_db(self) -> Optional[Database]:
        return self.db

# Global instance of the MongoDB connection manager
mongo_db_connection = MongoDBConnection()

# You can then use this instance in your application startup/shutdown events
# and import `mongo_db_connection.get_db()` in your CRUD operations modules.

# Example usage (typically in main.py or routers):
# from app.core.db import mongo_db_connection
# db = mongo_db_connection.get_db()
# if db:
#     my_collection = db["my_collection"]
#     # do something with my_collection
