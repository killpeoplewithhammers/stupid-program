#! /bin/python

from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=f"Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Click Here", command=root.destroy).grid(column=0, row=2)
root.mainloop()