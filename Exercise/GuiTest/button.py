import tkinter.messagebox
from tkinter import *

win = Tk()
win.title('Welcome')
win.geometry('500x200')

def func():
    tkinter.messagebox.showinfo("Greetings", "Hello! Welcome to PythonGeeks.")

btn = Button(win, text="Click Me!", width=10, height=5, command=func)
btn.place(x=200, y=30)

win.mainloop()

