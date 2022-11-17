from tkinter import *

class FieldButton(Button):
    idx = 0
    def __init__(self, master, idx, text="", fg="black", width=50, height=10):
        Button.__init__(self, master, text=text, fg=fg, width=width, height=height)
        self.idx = idx