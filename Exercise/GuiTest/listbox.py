from tkinter import *

win=Tk()
win.title("listbox")
win.geometry('300x100')

lb = Listbox(win)
for i in range(5):
    lb.insert(i, f'itemke{i*2}')
lb.pack()

win.mainloop()