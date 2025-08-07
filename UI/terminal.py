from customtkinter import CTkTextbox, CTkEntry, CTkFrame
from UI.styles import Color
from input_handler import InputHandler
from messages import Messages

class Terminal(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.handler = InputHandler(self)
        
        self.configure(fg_color=Color.sage)
        self.rowconfigure(list(range(10)), weight=1)
        self.columnconfigure(0, weight=1)
        
        self.viewport = CTkTextbox(self, state='disabled', fg_color=Color.cream, text_color=Color.burgundy)
        self.viewport.grid(row=0, rowspan=10, padx=5, pady=(5, 2.5), sticky='nsew')
        self.viewport_normal()
        self.viewport.insert('end', 'Use \'help\' to see possible command\n')
        self.viewport_disabled()
        
        self.entry = CTkEntry(self, fg_color=Color.cream, text_color=Color.burgundy)
        self.entry.grid(row=10, column=0, padx=5, pady=(2.5, 5), sticky='nsew')
        self.entry.bind('<Return>', self.on_enter)
        
    def on_enter(self, _=None):
        self.viewport_normal()
        input = self.get_entry()
        self.handler.process(input)
        self.viewport_disabled()
        self.clear_entry()
        
    def display_from_handler(self, input):
        self.viewport_normal()
        self.display_entry(input)
        self.viewport_disabled()
        
        
    def viewport_normal(self):
        self.viewport.configure(state='normal')
        
    def viewport_disabled(self):
        self.viewport.configure(state='disabled')
        
    def get_entry(self):
        return self.entry.get()
    
    def display_entry(self, input):
        self.viewport.insert('end', f'{input}\n')
        self.viewport.see('end')
        
    def clear_entry(self):
        self.entry.delete(0, 'end')
        
    def clear_viewport(self):
        self.viewport_normal()
        self.viewport.delete(0.0, 'end')
        self.viewport_disabled()
        