from tkinter import *
from PIL import ImageTk, Image


win = Tk()

image = Image.open('user.png')
image = ImageTk.PhotoImage(image)
label = Label(win, image=image)
label.pack(padx=40, pady=40)
win.mainloop()

