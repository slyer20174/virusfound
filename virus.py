from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning("ALERT", "STOP! VIRUS FOUND. YOU NEED TO DELETE ANY UNWANTED ITEMS INSIDE YOUR DEVICE")
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)
root.mainloop()