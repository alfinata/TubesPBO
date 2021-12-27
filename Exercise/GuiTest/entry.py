from tkinter import *
import tkinter.messagebox

win = Tk()
win.geometry('500x100')
win.title("test entry")

def func():
    tkinter.messagebox.showinfo(ent1.get(), ent2.get())

Label(win, text="Name").grid(row=0)
Label(win, text="email").grid(row=1)

ent1 = Entry(win)
ent2 = Entry(win)

ent1.grid(row=0, column = 1)
ent2.grid(row=1, column = 1)

btn = Button(win, text="Show inputs", width = 10, height=5, command=func)
btn.grid(row=2)

win.mainloop()