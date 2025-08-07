from commands import HelpCommand, LogCommand, CharCommand
from messages import Messages
from file_handler import FileHandler

class InputHandler:
    def __init__(self, master):
        self.master = master

        self.char = CharCommand(self.master)
        self.help = HelpCommand
        self.log = LogCommand(self.master)
        self.file_handler = FileHandler()
        
        self.tag: str = None
        self.primary_tag: str = None
        self.secondary_tag: str = None
        self.value: str = None
        
        self.input: list[str] = None

    def process(self, input: str):
        
        self.split_tag(input)
        if self.primary_tag == 'char':
            self.char.process_tag(self.input)
        elif self.primary_tag == 'clear':
            self.master.clear_viewport()
        elif self.primary_tag == 'help':
            self.help_command()
        elif self.primary_tag == 'log':
            self.log.process_tag(self.input)
        else:
            self.master.display_entry(f'{Messages.invalid_tag} ({self.tag})')
            
        self.tag: str = None
        self.primary_tag: str = None
        self.secondary_tag: str = None
        self.value: str = None
            
    def split_tag(self, input: str):
        input = input.lower().strip()
        
        if len(input.split(':', 1)) == 2:
            self.tag, self.value = input.split(':', 1)
        else:
            if input.endswith(':'):
                self.tag = input[0:-1]
            else:
                self.tag = input
            
        if len(self.tag.split('.')) == 2:
            self.primary_tag, self.secondary_tag = self.tag.split('.')
        else:
            self.primary_tag = self.tag
            
        self.input = [self.primary_tag, self.secondary_tag, self.value]

    def help_command(self):
        self.master.display_entry(self.help.get_text())

        