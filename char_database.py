import sqlite3

class CharDatabase:
    def __init__(self):
        self.char_name: str = None
        self.conn = None
        self.cursor = None
        
        self.create_attributes = '''Charisma INTEGER NOT NULL,
                                            Constitution INTEGER NOT NULL,
                                            Dexterity INTEGER NOT NULL,
                                            Intelligence INTEGER NOT NULL,
                                            Strength INTEGER NOT NULL,
                                            Wisdom INTEGER NOT NULL'''
        
    def create_character_db(self, value):
        self.char_name = value
        self.conn = sqlite3.connect(self.char_name)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute(f'CREATE TABLE IF NOT EXISTS {self.char_name} ({self.create_attributes})')