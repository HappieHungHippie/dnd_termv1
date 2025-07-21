
class HelpCommand:
    def __init__(self):
        pass
    
    @staticmethod
    def get_text():
        with open('info\help.txt', 'r') as file:
            return file.read()