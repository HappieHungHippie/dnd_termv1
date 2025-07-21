from commands import HelpCommand
from messages import Messages

class InputHandler:
    def __init__(self, master):
        
        self.input: str = None
        
        self.master = master
        self.commands = ['create', 
                         'help', 
                         'log']
        
    def process(self, input: str):
        input = input.lower().strip()
        input_split = input.split(':', 1)
        if input_split[0] == 'create':
            print('Create Character')
        if input_split[0] == 'help':
            self.help_command()
        if input_split[0] == 'log':
            if len(input_split) == 2:
                print(input_split[1])
                
    def help_command(self):
        self.master.display_from_handler(HelpCommand.get_text())
        
    def check_if_command(self, input):
        if input in self.commands:
            return True
        else:
            self.master.display_entry(Messages.invalid_tag)
        