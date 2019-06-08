from tkinter import *
from tkinter import messagebox as box

# designe start ----->
def main_menu():
# ---window initalization---
    window = Tk()
#----window title--------
    window.title('ALISHA PC SOFTWARE')
    window.geometry('480x600')
    window.configure(background = 'BLUE')
    label = Label(window, text = 'ALISHA EMBEDDEDSOFT',bd=10,padx=500, fg = 'white',pady=16, bg = 'RED', font = (None, 11), height = 1)
    label.pack(side = TOP)

#-----DISPLAY VARIABLE TO SET AS SCREEN-------
    var = StringVar()
    #label = Label(window, text = 'DISPLAY',bd=10,padx=100, fg = 'BLACK',pady=16, bg = 'yellow', font = (None, 11), height = 1)
    label = Message( window, textvariable = var, relief = RAISED )
    var.set("*-----DISPLAY----*\n COUNTER:6 \n TOKEN:999\n")
    label.pack()
    button1=Button(window,padx=16,pady=16,bd=8,text="1",fg="black")
    button1.pack(side=LEFT)
    button1=Button(window,padx=16,pady=16,bd=8,text="2",fg="black")
    button1.pack(side=LEFT)
    button1=Button(window,padx=16,pady=16,bd=8,text="3",fg="black")
    button1.pack(side=LEFT)
    button1=Button(window,padx=16,pady=16,bd=8,text="wait",fg="black")
    button1.pack(side=LEFT)
    button1=Button(window,padx=16,pady=16,bd=8,text="c-1",fg="black")
    button1.pack(side=LEFT)
    





main_menu()
