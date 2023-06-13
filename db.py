from pymongo import MongoClient

# Read Mongo API key from a txt file
with open('db-api-key.txt', 'r') as file:
     uri = file.readline().strip()

def create_client():
    client = MongoClient(uri)
    return client

def get_db(client):
    # This function returns the database object which you will use to interact with the database
    db = client['movies1']
    return db

def close_client(client):
    # Always close when done
    client.close()