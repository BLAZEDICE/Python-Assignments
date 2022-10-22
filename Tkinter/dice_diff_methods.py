from argparse import Action
from tkinter import *
import tkinter
from PIL import Image,ImageTk
import random
from tkinter import messagebox
root=Tk()
root.geometry("1000x800")

# # main_dice=Image.open(f"E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")
# # main_dice_show=ImageTk.PhotoImage(image=main_dice)
# # label1=Button(root,image=main_dice_show,borderwidth=5,background="black" ,foreground="Blue").pack(pady=100)
# # main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")

# def throw():
#     rand_no=random.randint(1,6)
#     main_dice=Image.open(f"E:\\python programs\\Adv_Python\\Tkinter\\dice{rand_no}.png")
#     main_dice_show=ImageTk.PhotoImage(image=main_dice)
#     # main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")
#     # label1=Button(root,image=main_dice_show,borderwidth=5,background="black" ,foreground="Blue").pack(pady=100)
#     label2=Label(root,image=main_dice_show,borderwidth=5).pack(pady=100)


# def throw2():
#     rand_no=random.randint(1,6) 
#     if(rand_no==1):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")
#         print("You rolled no 1")

#     if(rand_no==2):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice2.png")
#         print("You rolled no 2")

#     if(rand_no==3):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice3.png")
#         print("You rolled no 3")

#     if(rand_no==4):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice4.png")
        
#     if(rand_no==5):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice5.png")

#     if(rand_no==6):
#         main_dice_show=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice6.png")

# # label1=Button(root,text="click",borderwidth=5,foreground="Blue",command=throw2).pack(pady=100)

# d1=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice1.png")
# d2=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice2.png")
# d3=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice3.png")
# d4=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice4.png")
# d5=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice5.png")
# d6=PhotoImage(file="E:\\python programs\\Adv_Python\\Tkinter\\dice6.png")
# mychoice=[d1,d2,d3,d4,d5,d6]
# side=random.choice(mychoice)
# def myfunc():
#     side2=random.choice(mychoice)
#     print(side2)
#     Label(root,image=side2).place(x=180,y=30)
# mybutton=Button(root,image=side,command=myfunc).place(x=250,y=250)

rand_no=random.randint(1,6)
main_dice_show=PhotoImage(file=f"E:\\python programs\\Adv_Python\\Tkinter\\dice{rand_no}.png")
def throw():
    rand_no=random.randint(1,6)
    # main_dice=Image.open(f"E:\\python programs\\Adv_Python\\Tkinter\\dice{rand_no}.png")
    # main_dice_show=ImageTk.PhotoImage(image=main_dice)\
    global main_dice_show
    main_dice_show=PhotoImage(file=f"E:\\python programs\\Adv_Python\\Tkinter\\dice{rand_no}.png")
    # label1=Button(root,image=main_dice_show,borderwidth=5,background="black" ,foreground="Blue").pack(pady=100)
    Label(root,image=main_dice_show).place(x=220,y=40)
    Label(root,text=f"You rolled {rand_no}").place(x=340,y=300)
    mybutton=Button(root,image=main_dice_show,command=throw).place(x=340,y=450)
    
    print(main_dice_show)

mybutton=Button(root,image=main_dice_show,command=throw).place(x=340,y=450)


root.mainloop()
