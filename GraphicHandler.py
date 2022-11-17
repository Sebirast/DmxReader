from tkinter import *
from Widget import *
from FieldButton import *

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
        
        self.fieldBottomLeftButton = FieldButton(self.bottomframe, 0, text="+", fg="brown", width=50, height=10)
        self.fieldBottomLeftButton.pack(side = "top")

        self.fieldTopLeftButton = FieldButton(frame, 1, text="+", fg="red", width=50, height=10)
        self.fieldTopLeftButton.pack( side = LEFT)

        self.fieldTopRightButton = FieldButton(frame, 2, text="+", fg="blue", width=50, height=10)
        self.fieldTopRightButton.pack( side = LEFT )

        self.bottomRightFrame = Frame(self.master, width=50)
        self.bottomRightFrame.pack(side=RIGHT)

        self.fieldButtonRightButton = FieldButton(self.bottomRightFrame, 3, text="+", width=50, height=10)
        self.fieldButtonRightButton.pack( side = RIGHT)
        
        wi =  MyWidget(self.bottomRightFrame)
        wi.pack(side = "left")

    def makeGUI(self) -> None:
        self.widgets.append(Widget(self.master))

    def _onFieldButtonPress(self, buttonIdx) -> None:
        pass

    def loop(self) -> None:
        self.master.update_idletasks()
        self.master.update()