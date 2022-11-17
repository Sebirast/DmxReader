from tkinter import *

class MyWidget(Frame):
    def __init__(self, master, background="#000000", width=100) -> None:
        Frame.__init__(self, master, background=background, width=width)
        inputBox = Entry(self, width=50,text="hello world")
        outputBox = Entry(self, width=50)
        inputBox.pack(side="left")
        outputBox.pack(side="left")