"""
ALISHA PROJECT 29 JULY 2018 5:46
"""

import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *


class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with    fullscreen.
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
 
        label = Label(self.tk,anchor="center",bg="green")
        label.grid(column=0,row=0,sticky='NSEW')

        label2 = Label(self.tk,anchor="center",bg="black")
        label2.grid(column=1,row=0,sticky='NSEW')

        label3 = Label(self.tk,anchor="center",bg="red")
        label3.grid(column=2,row=0,sticky='NSEW')

        label4 = Label(self.tk,anchor="center",bg="purple")
        label4.grid(column=0,row=1,sticky='NSEW')

        label5 = Label(self.tk,anchor="center",bg="blue")
        label5.grid(column=1,row=1,sticky='NSEW')

        label6 = Label(self.tk,anchor="center",bg="yellow")
        label6.grid(column=2,row=1,sticky='NSEW')


        self.tk.grid_columnconfigure(0,weight=1)
        self.tk.grid_columnconfigure(1,weight=1)
        self.tk.grid_columnconfigure(2,weight=1)
        self.tk.grid_rowconfigure(0,weight=1)
        self.tk.grid_rowconfigure(1,weight=1)
   
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
 

    

if __name__ == '__main__':
    w = Fullscreen_Window()
    w.tk.mainloop()
