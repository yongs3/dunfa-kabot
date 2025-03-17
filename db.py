from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
DB_NAME = os.getenv('DB_NAME', 'dunfa_db')

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[DB_NAME]
        self.adventures = self.db.adventures
        self.characters = self.db.characters
    
    def add_adventure(self, adventure_name):
        adventure = self.adventures.find_one({'name': adventure_name})
        if not adventure:
            result = self.advantures.insert_one({
                'name': adventure_name,
                'count': 0,
                'created_at': datetime.now()
            })
            adventure_id = result.inserted_id
            return {'_id': adventure_id, 'name': adventure_name, 'count': 0}
        return adventure
    
    def add_character(self, character_name, adventure_name):
        adventure = self.add_adventure(adventure_name)

        existing_character = self.characters.find_one({'name': character_name, 'adventure_id': adventure['_id']})

        if existing_character:
            return existing_character['_id']
        
        character_data = {
            'adventure_id': adventure['_id'],
            'name': character_name,
            'created_at': datetime.now()
        }

        result = self.characters.insert_one(character_data)
        self.adventures.update_one({'_id': adventure['_id']}, {'$inc': {'count': 1}})

        return result.inserted_id
        
    
    def get_charaters_by_adventure(self, adventure):
        adventure = self.adventures.find_one({'name': adventure})
        if not adventure:
            return None
        
        characters = self.characters.find({'adventure_id': adventure['_id']})

        return list(characters)
    
    def get_character_by_name(self, character_name):
        character = self.characters.find_one({'name': character_name})
        return character

mongo_db = MongoDB()