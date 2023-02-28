#! /bin/python

from tkinter import *
from tkinter import ttk
import time

# Variables
clickArray = []

# Functions

# Function that runs whenever the button is clicked
def click():
    currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
    clickArray.append(currentTime)
#    updateClickSpeed()
    print("clickfunc: " + str(len(clickArray)))

# Function to remove clicks that are over a second old
def updateClickSpeed():
    currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
    for clickNumber in range(len(clickArray)-1):
        if clickArray[0] + 1000000000 < currentTime:
            clickArray.pop(0)
            label.configure(text=f"{len(clickArray)} click per second")
            print("update: " + str(len(clickArray)))
    Label.after(50, updateClickSpeed)
#        else:
#            print(clickArray)
#            print(clickNumber)
#            break


tk = Tk()
frm = ttk.Frame(tk, padding=100)
frm.grid()

label = ttk.Label(frm, text="0 cps", command=updateClickSpeed())
label.grid(column=0, row=0)

ttk.Button(frm, text="Click Fast", command=click).grid(column=0, row=1)

# Loop
tk.mainloop()