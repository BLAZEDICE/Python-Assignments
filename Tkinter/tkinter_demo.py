# import tkinter
# window=tkinter.Tk()
# window.mainloop()

from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("500x500")

def fun():
    messagebox.showinfo("Hello","Red Button Clicked")

b1=Button(top,text="Red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=Button(top,text="Blue",activeforeground="blue",activebackground="pink",pady=10,bd=5)
b3=Button(top,text="Green",activeforeground="green",activebackground="pink",pady=10,border=5)
b4=Button(top,text="Yellow",activeforeground="yellow",activebackground="pink",pady=10,border=5)

b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)
top.mainloop()