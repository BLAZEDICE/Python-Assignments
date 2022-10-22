# from tkinter import *
# window=Tk()
# l1=Label(window,text="Gujarat University",font="Arial Bold",20)
import sys
print(sys.executable)
from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.geometry("900x700")
logo=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\pngwing.com.png")
# image=Image.open("E:\\python programs\\Adv_Python\\Tkinter\\songs.jpg")
# logo=ImageTk.PhotoImage(image)
w1=Label(root,image=logo).pack(side="right")
msg="Welcome Sem 3"
w2=Label(root,justify=LEFT,padx=10,text=msg).pack(side="left")
root.mainloop()