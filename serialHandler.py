#!/usr/bin/env python3
import serial
from tkinter import messagebox

# class that handles all serial outputs and inputs
class SerialHandler():

    ser = None
    
    # constructor: the serial port is set
    def __init__(self):
        try:
            self.ser = serial.Serial('/dev/ttyACM1', 115200, timeout=1)
        except:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

        self.ser.reset_input_buffer()
    
    # this funciton sends a index to the arduino. when the arduino sends a message back it unpacks and decodes that message. after that the message is returned. channel is the message that is to be sent to the arduino
    def getValue(self, channel) -> str:
        try:
            print(int(channel))
            if(int(channel) > 512):
                messagebox.showwarning(title="DMX-Overflow", message="Max channel is 512") 
                print(lol)
                return
        except Exception as e: print(e)

        # print("entered get value")
        output = bytes(channel + "\n", 'utf-8')
        self.ser.write(output)
        line = self.ser.readline().decode('utf-8').strip()
        # output = self.ser.readline().decode('utf-8')
        print(line)
        # print("finished")
        return line