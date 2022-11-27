import os
from GraphicHandler import * 
from serialHandler import *
import time

if os.environ.get('DISPLAY', '') == '':
  print('no display found. using: 0.0')
  os.environ.__setitem__('DISPLAY', ':0.0')

def checkTime(freq):
    global currentTime, lastLoopTime
    currentTime = time.time()

    if float(currentTime) - float(lastLoopTime) > freq:
        lastLoopTime = currentTime
        return True
    return False

serial = SerialHandler()

master = Tk()
Label(master, text="Channel").grid(row=0)
Label(master, text="Value").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
# e2.config(state = "disabled")
e1.insert(0, "2")

b1 = Button(master, text="Go", command=lambda: getValueWrapper()).grid(column=2, row=0)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def getValueWrapper():
    e2.delete(0)
    e2.insert(0, serial.getValue(e1.get()))

lastLoopTime = time.time()

lastindex = e1.get()
# lastValue = serial.getValue(e1.get())

while True:
    if(checkTime(7.5e-5)):
        if(lastindex != e1.get()):
            getValueWrapper()
            lastindex = e1.get()
        master.update_idletasks()
        master.update()
        # if lastValue != serial.getValue(e1.get()):
        #     getValueWrapper()
        #     lastValue = serial.getValue(e1.get())
        print("hello world")