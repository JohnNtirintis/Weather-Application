from pymongo import MongoClient

# Read Mongo API key from a txt file
with open('db-api-key.txt', 'r') as file:
     uri = file.readline().strip()

def create_client():
    client = MongoClient(uri)
    return client

def get_db(client):
    db = client['users']
    return db

def get_collection(db):
    col = db['users-credentials']

def close_client(client):
    # Always close when done
    client.close()