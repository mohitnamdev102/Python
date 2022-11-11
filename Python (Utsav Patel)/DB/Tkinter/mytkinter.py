# import tkinter as tk
from tkinter import *
from tkinter import ttk
# win = Tk()
# label1 = ttk.Label(win, text="Username")
# label2 = ttk.Label(win, text="Password")
#
# ent1 = ttk.Entry(win)
# ent2 = ttk.Entry(win, show='\u2022')
#
# label1.pack(padx=10, pady=10)
# ent1.pack(padx=10, pady=10)
# label2.pack(padx=10, pady=10)
# ent2.pack(padx=10, pady=10)
#
# def mybtn(event):
#     user = ent1.get()
#     passw = ent2.get()
#     labelnew  = Label(win,text=user)
#     labelnew.pack()
#
# btn = ttk.Button(win, text='Login')
#
# btn.bind("<Button-1>", mybtn)
#
# btn.pack(padx=10, pady=10)
#
# # win.geometry('1200x900')
# win.mainloop()
#


win = Tk()


def newWin(event):

    u = str(ent1.get())
    p = str(ent2.get())

    if u == "" or p == "":
        l = Label(win, text="Eiter password or username missing!", fg='red')
        l.grid(columnspan=2)
    elif u == "utsav" and p == "abc@1234":
        win.withdraw()
        newWindow = Tk()
        t = "welcome " + u
        label = Label(newWindow, text=t)
        label.pack()
        newWindow.mainloop()



label1 = Label(win, text="Username")
label2 = Label(win, text="Password")
ent1 = Entry(win)
ent2 = Entry(win, show='\u2022')

label1.grid(row=0, column=0, padx=10, pady=5)
label2.grid(row=1, column=0, padx=10, pady=5)
ent1.grid(row=0, column=1, padx=10, pady=5)
ent2.grid(row=1, column=1, padx=10, pady=5)

btn = Button(win, text='Login')
btn.bind('<Button-1>', newWin)
btn.grid(columnspan=2, padx=10, pady=5)
win.mainloop()
