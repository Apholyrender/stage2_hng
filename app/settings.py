from decouple import config



DATABASE_NAME = config("DATABASE_NAME")
DATABASE_URI = config("DATABASE_URI")
COLLECTION_NAME = config("COLLECTION_NAME")