from pathlib import Path


class CharacterHandler:
    def __init__(self):
        self.chardir = Path('characters_directory')
        self.chardir.mkdir(exist_ok=True)

        self.charlist: list = []

        self.load_characters()
        self.get_characters()

    def load_characters(self):
        self.charlist.clear()
        for char in self.chardir.iterdir():
            if char.is_file():
                char = char.name.capitalize()
                self.charlist.append(char)

    def get_characters(self):
        return self.charlist
    