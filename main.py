#! /bin/python

from tkinter import *
from tkinter import ttk
import time

clickarray = []
def click(clickarray):
    clickarray = clickarray + [time.clock_gettime_ns(time.CLOCK_REALTIME)]
    print(clickarray)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=f"you click ").grid(column=0, row=0)
ttk.Button(frm, text="Click Fast", command=).grid(column=0, row=1)
root.mainloop()
print("time is", time.clock_gettime_ns(time.CLOCK_REALTIME)