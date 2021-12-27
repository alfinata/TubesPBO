from tkinter import *
win=Tk() #creating the main window and storing the window object in 'win'
win.geometry('300x150')
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

help_menu = Menu(mn) 
mn.add_cascade(label='Help', menu=help_menu) 
help_menu.add_command(label='Feedback') 
help_menu.add_command(label='Contact') 

win.mainloop() #running the loop that works as a trigger