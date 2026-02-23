import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/lexassist")

_client = None
_db = None


def get_db():
    """Get the MongoDB database instance (singleton)."""
    global _client, _db
    if _db is None:
        _client = MongoClient(MONGO_URI)
        db_name = MONGO_URI.rsplit("/", 1)[-1].split("?")[0]
        _db = _client[db_name]
        # Ensure unique index on email
        _db.users.create_index("email", unique=True)
    return _db


def get_users_collection():
    """Return the users collection."""
    return get_db().users
