from tkinter import *
win=Tk() #creating the main window and storing the window object in 'win'
win.geometry('300x100')
var = IntVar() 
Radiobutton(win, text='Male', variable=var, value=1).pack(anchor=W) 
Radiobutton(win, text='Female', variable=var, value=2).pack(anchor=W) 
Radiobutton(win, text='Other', variable=var, value=3).pack(anchor=W) 
win.mainloop() #running the loop that works as a trigger