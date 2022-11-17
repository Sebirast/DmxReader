import os
from GraphicHandler import * 

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

# def sendIndex():

gfx = GraphicHandler()

while True:
    gfx.loop()