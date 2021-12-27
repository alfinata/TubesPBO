from tkinter import *
import tkinter.messagebox

# Main Window
win=Tk()
win.title('TestGame')
win.geometry('300x200')

# Menus
mn = Menu(win) 
win.config(menu=mn) 

file_menu = Menu(mn, tearoff=0) 
mn.add_cascade(label='File', menu=file_menu) 
file_menu.add_command(label='New') 
file_menu.add_command(label='Open...') 
file_menu.add_command(label='Save') 
file_menu.add_separator() 
file_menu.add_command(label='About') 
file_menu.add_separator() 
file_menu.add_command(label='Exit', command=win.quit) 

help_menu = Menu(mn, tearoff=0) 
mn.add_cascade(label='Help', menu=help_menu) 
help_menu.add_command(label='Feedback') 
help_menu.add_command(label='Contact') 

# Input Nama
nameFrame = Frame(win)
nameFrame.grid(row=0)

Label(nameFrame, text="Name", width = 10, height = 3).pack(side=LEFT)
ent1 = Entry(nameFrame, width = 30)
ent1.pack(side=LEFT)

# Input Class
classFrame = Frame(win)
classFrame.grid(row=1)

Label(classFrame, text="Class",  width = 10, height = 3).pack(side=LEFT)

var = IntVar() 
rd1 = Radiobutton(classFrame, variable=var, text='Warrior', value = 1)
rd1.pack(side=LEFT)
rd2 = Radiobutton(classFrame, variable=var, text='Mage', value = 2)
rd2.pack(side=LEFT)
rd3 = Radiobutton(classFrame, variable=var, text='Thief', value = 3)
rd3.pack(side=LEFT)

# Button

def submit():
    tkinter.messagebox.showinfo("Player info", "Welcome to the game!")

btn = Button(win, text="continue", width = 10, height=2, command=submit)
btn.grid(row=2)

win.mainloop() #running the loop that works as a trigger