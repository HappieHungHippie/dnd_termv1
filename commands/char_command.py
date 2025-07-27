from char_database import CharDatabase

class CharCommand:
    def __init__(self):
        self.database = CharDatabase()
    
    def process_tag(self, tag: list[str]):
        primary, secondary, value = tag
        if secondary == 'create':
            self.create(value)
        
    def create(self, value):
        self.database.create_character_db(value)