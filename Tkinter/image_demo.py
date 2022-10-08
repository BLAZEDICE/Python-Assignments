# from tkinter import *
# window=Tk()
# l1=Label(window,text="Gujarat University",font="Arial Bold",20)
from tkinter import *
import tkinter 
root=Tk()
logo=tkinter.PhotoImage(file="test.png")
w1=Label(root,image=logo).pack(side="right")
msg="Welcome Sem 3"
w2=Label(root,justify=tkinter.LEFT,padx=10,text=msg).pack(side="left")
root.mainloop()