from tkinter import *
root=Tk()
root.geometry("500x300")

def submit():
    myten=ten_val.get()
    mycric=cric_val.get()
    Label(root,text=f"Your gender is {gend_val.get()}").place(x=170,y=160)
    if(mycric and myten):
        Label(root,text=f"Your hobby is cricket and tennis").place(x=170,y=190)
    elif(mycric):
        Label(root,text=f"Your hobby is cricket").place(x=170,y=190)
    elif(myten):
        Label(root,text=f"Your hobby is tennis").place(x=170,y=190)
   
    else:
        ""

gend_val=StringVar()
mal_but=Radiobutton(root,text="Male",variable=gend_val,value="Male")
femal_but=Radiobutton(root,text="Female",variable=gend_val,value="Female")
mal_but.place(x=100,y=50)
femal_but.place(x=200,y=50)
gend_val.set(0)
cric_val=IntVar()
cricket=Checkbutton(root,text="Cricket",variable=cric_val,onvalue=1,offvalue=0,height=2,width=10)
cricket.place(x=84,y=85)
ten_val=IntVar()
tennis=Checkbutton(root,text="Tennis",variable=ten_val,onvalue=1,offvalue=0,height=2,width=10)
tennis.place(x=184,y=85)
sub_btn=Button(root,text="Submit",command=submit).place(x=170,y=130)




root.mainloop()