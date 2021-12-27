from tkinter import *

win = Tk()
win.geometry("300x100")
win.title("Frame")

frame = Frame(win, width = '150', height = '100', bg="yellow")
frame.pack(side=LEFT)

second_frame = Frame(win)
second_frame.pack(side = RIGHT)

red_button = Button(frame, text="Hello", bg='red', fg ="black")
red_button.pack(side=LEFT)

green_button = Button(frame, text="Hi!", bg="green", fg="white")
green_button.pack(side=LEFT)

blue_button = Button(second_frame, text="Blue", bg = "blue", fg="white")
blue_button.pack(side=LEFT)

win.mainloop()