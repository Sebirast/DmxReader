from tkinter import *

class MyWidget(Frame):
    def __init__(self, master, background="#000000", width=100):
        Frame.__init__(self, master, background=background, width=width)