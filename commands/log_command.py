from messages import Messages
from pathlib import Path

class LogCommand:
    def __init__(self, master):
        self.master = master
        self.log_text = None
        self.file_name = Path('info/log.txt')
        self.initialize_log()

    def process_tag(self, tag: list[str]):
        primary, secondary, value = tag
        if secondary is None:
            self.append_to_log(value)
        elif secondary == 'delete':
            self.delete_last_line()
        elif secondary == 'delete_all':
            self.delete_all()
        elif secondary == 'read':
            self.master.master.display_from_handler(self.get_text())
        else:
            self.master.master.display_from_handler(f'{Messages.invalid_secondary} ({secondary})')

    def append_to_log(self, value: str):
        value = value.strip()
        with open(self.file_name, 'a') as log:
            log.write(f'{value}\n')

    def delete_last_line(self):
        with open(self.file_name, 'r') as log:
            lines = log.readlines()
        if lines:
            lines.pop()
            with open(self.file_name, 'w') as log:
                log.writelines(lines)
                
    def delete_all(self):
        with open(self.file_name, 'w') as log:
            pass

    def get_text(self):
        self.read_log()
        return f'--------\n{self.log_text}--------'

    def initialize_log(self):
        self.file_name.parent.mkdir(parents=True, exist_ok=True)
        self.file_name.touch(exist_ok=True)
        self.read_log()

    def read_log(self):
        with open(self.file_name, 'r') as log:
            self.log_text = log.read()
