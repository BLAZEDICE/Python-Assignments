from tkinter import *
root=Tk()
root.geometry("500x500")
lab1=Label(root,text="Enter value of integer n")
lab1.pack()

int_val=IntVar()
int_inp=Entry(root,textvariable=int_val)
int_inp.pack()


def validate():
    result=0
    myval=int_val.get()
    for i in range(1,myval+1):
        result=result+i

    Label(root,text=f"The sum is 1 + 2 + 3 + ... + 5 = {result}").pack()

val_but=Button(root,text="Validate",width=15,command=validate)
myvar=StringVar(root)
myopt=OptionMenu(root,myvar,"One","Two","Three").pack()
val_but.pack()
root.mainloop()

