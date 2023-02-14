#! /bin/python

from tkinter import *
from tkinter import ttk
from functools import partial
import time

clickArray = []
def click(clickArray):
    currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
    clickArray.append(currentTime)
    for clickNumber in range(len(clickArray)-1):
        if clickArray[clickNumber] + 1000000000 < currentTime:
            clickArray.pop(clickNumber)
        else:
            break
    return clickArray
    
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text=f"you click {len(clickArray)}").grid(column=0, row=0)
ttk.Button(frm, text="Click Fast", command=partial(click, clickArray)).grid(column=0, row=1)
root.mainloop()