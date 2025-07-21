
class LogCommand:
    def __init__(self):
        self.log_text = None
        
        self.initialize_log()
    
    def initialize_log(self):
        with open('info\\log.txt', 'r') as log:
            self.log_text = log.read()
        print(self.log_text)
        
    def get_text(self):
        return f'--------\n{self.log_text}\n--------'