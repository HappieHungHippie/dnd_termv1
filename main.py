from customtkinter import CTk
from UI import Terminal

class App(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        self.geometry('800x500')
        
        self.terminal = Terminal(self)
        self.terminal.pack(fill='both', expand=True)
        

if __name__ == '__main__':
    program = App()
    program.mainloop()