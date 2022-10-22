from argparse import Action
from tkinter import *
from PIL import Image,ImageTk
import random
from tkinter import messagebox
root=Tk()
root.geometry("700x500")


d1=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")
d2=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice2.png")
d3=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice3.png")
d4=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice4.png")
d5=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice5.png")
d6=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice6.png")
mychoice=[d1,d2,d3,d4,d5,d6]
side=random.choice(mychoice)
def myfunc():
    side2=random.choice(mychoice)
    print(side2)
    Label(root,image=side2).place(x=180,y=30)
mybutton=Button(root,image=side,command=myfunc).place(x=250,y=250)

root.mainloop()
