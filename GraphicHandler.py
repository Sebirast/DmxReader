from tkinter import *
from widget import *

class GraphicHandler:
    master = None
    bottomframe = None
    bottomRightFrame = None
    widgets = []

    def __init__(self) -> None:
        self.master = Tk()
        self.master.title("DmxReader")
        self.master.geometry("800x410")

        frame = Frame(self.master)
        frame.pack()

        self.bottomframe = Frame(self.master, background="#000000", width=100)
        self.bottomframe.pack(side = LEFT)
        
        self.fieldBottomLeftButton = Button(self.bottomframe, text="Brown", fg="brown", width=50, height=10)
        self.fieldBottomLeftButton.pack(side = "top")

        self.fieldTopLeftButton = Button(frame, text="Red", fg="red", width=50, height=10)
        self.fieldTopLeftButton.pack( side = LEFT)

        self.fieldTopRightButton = Button(frame, text="Blue", fg="blue", width=50, height=10)
        self.fieldTopRightButton.pack( side = LEFT )

        self.bottomRightFrame = Frame(self.master, width=100)
        self.bottomRightFrame.pack(side=RIGHT)

        self.fieldButtonRightButton = Button(self.bottomRightFrame, text="Black", fg="black",  width=50, height=10)
        self.fieldButtonRightButton.pack( side = RIGHT)

    def makeGUI(self) -> None:
        self.widgets.append(Widget(self.master))

    def _onFieldButtonPress(self) -> None:
        pass

    def loop(self) -> None:
        self.master.update_idletasks()
        self.master.update()