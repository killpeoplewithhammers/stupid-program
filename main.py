#! /bin/python

from tkinter import *
from tkinter import ttk
from functools import partial
import time

clickArray = []
def click():
    currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
    clickArray.append(currentTime)
    updateClickSpeed()
    print(len(clickArray))

def updateClickSpeed():
    currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
    for clickNumber in range(len(clickArray)-1):
        if len(clickArray) < 1:
            break
        elif clickArray[0] + 1000000000 < currentTime:
            print("clicknumber is ", clickNumber)
            clickArray.pop(0)
        else:
            break
    
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="you click (put click speed here)").grid(column=0, row=0)
ttk.Button(frm, text="Click Fast", command=partial(click)).grid(column=0, row=1)
root.mainloop()