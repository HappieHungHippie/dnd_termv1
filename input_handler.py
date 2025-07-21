from commands import HelpCommand, LogCommand
from messages import Messages

class InputHandler:
    def __init__(self, master):
        self.master = master
        self.input: str = None

        self.help = HelpCommand
        self.log = LogCommand()

        self.commands = ['clear', 'create', 'help', 'log', 'read_log']

    def process(self, input: str):
        input = input.lower().strip()
        input_split = input.split(':', 1)
        command = input_split[0]

        if command == 'clear':
            self.master.clear_viewport()
        elif command == 'create':
            print('Create Character')
        elif command == 'help':
            self.help_command()
        elif command == 'log':
            if len(input_split) == 2:
                print(input_split[1])
        elif command == 'read_log':
            self.master.display_from_handler(self.log.get_text())
        else:
            self.master.display_entry(Messages.invalid_tag)

    def help_command(self):
        self.master.display_from_handler(self.help.get_text())

    def check_if_command(self, input):
        return input in self.commands

        