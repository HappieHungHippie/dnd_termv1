
class HelpCommand:
    
    @staticmethod
    def get_text():
        with open('info\\help.txt', 'r') as file:
            return file.read()