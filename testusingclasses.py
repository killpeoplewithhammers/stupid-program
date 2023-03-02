import tkinter as tk
from tkinter import ttk
import time


class DigitalClock(tk.Tk):

    def __init__(self):
        super().__init__()
        self.clickArray = []
        # configure the root window
        self.title('click speed test')

        # label
        self.label = ttk.Label(
            self,
            text="0")
        self.label.pack(expand=True)

        # button
        self.button = ttk.Button(
            self,
            text="Click Here!",
            command=self.click
        )
        self.button.pack(expand=True)

        # schedule an update every 100th of a second
        self.label.after(100, self.update)

    def click(self):
        currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
        self.clickArray.append(currentTime)

    def updateClickSpeed(self):
        currentTime = time.clock_gettime_ns(time.CLOCK_REALTIME)
        for i in range(len(self.clickArray)-1):
            if self.clickArray[0] + 1000000000 < currentTime:
                self.clickArray.pop(0)
                return f"{len(self.clickArray)} click per second"

    def update(self):
        self.label.configure(text=self.updateClickSpeed())

        # schedule another timer ()
        self.label.after(100, self.update)


if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()