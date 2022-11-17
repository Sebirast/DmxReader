from tkinter import *

class Widget:
    def __init__(self, master) -> None:
        inputBox = Entry(master, width=50)
        outputBox = Entry(master, width=50)
        inputBox.pack(side="left")
        outputBox.pack(side="left")