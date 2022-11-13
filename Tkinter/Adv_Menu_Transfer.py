from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("700x700")

def b1():
    choice=lb.curselection()
    for i in choice[::-1]:
        print(i)
        items=lb.get(i)
        lb2.insert(END,items)
        lb.delete(i)
       

def b3():
    choice=lb2.curselection()
    for i in choice[::-1]:
        print(i)
        items=lb2.get(i)
        lb.insert(END,items)
        lb2.delete(i)


def b2():
    selec=lb.select_set(0,END)
    choice=lb.curselection()
    for i in choice[::-1]:
        print(i)
        items=lb.get(i)
        lb2.insert(END,items)
        lb.delete(i)


def b4():
    selec=lb2.select_set(0,END)
    choice=lb2.curselection()
    for i in choice[::-1]:
        print(i)
        items=lb2.get(i)
        lb.insert(END,items)
        lb2.delete(i)
    

def bill():
    selec=lb2.select_set(0,END)
    choice=lb2.curselection()
    bill=0
    for i in choice[::-1]:
        print(i)
        items=lb2.get(i)
        print(items)
        sliceditems=int(items[-3:])
        bill+=sliceditems
        print(sliceditems)
    messagebox.showinfo("Bill",f"Your bill is Rs.{bill}")
       

myscroll=Scrollbar(root)
myscroll.grid(row=0,column=1,rowspan=4,sticky=NS)

myscroll1=Scrollbar(root)
myscroll1.grid(row=0,column=4,rowspan=4,sticky=N+S)

lb=Listbox(root,width=20,height=15,bg="Red",font="Arial 14",fg="White",selectmode=MULTIPLE,yscrollcommand=myscroll.set)
lb.grid(row=0,column=0,rowspan=4)


lb2=Listbox(root,width=20,height=15,bg="Red",font="Arial 14",fg="White",selectmode=MULTIPLE,yscrollcommand=myscroll1.set)
lb2.grid(row=0,column=3,rowspan=4)

b=Button(root,text=">",font=("ArialBold",12),width=7,height=1,bd=3,command=b1)
b.grid(row=0,column=2,padx=20)
b1=Button(root,text=">>",font=("ArialBold",12),width=7,height=1,bd=3,command=b2)
b1.grid(row=1,column=2,padx=40)
b2=Button(root,text="<",font=("ArialBold",12),width=7,height=1,bd=3,command=b3)
b2.grid(row=2,column=2,padx=40)
b3=Button(root,text="<<",font=("ArialBold",12),width=7,height=1,bd=3,command=b4)
b3.grid(row=3,column=2,padx=40)
b4=Button(root,text="+",font=("ArialBold",12),width=7,height=1,bd=3,command=bill)
b4.grid(row=4,column=2,padx=40)



myscroll.config(command=lb.yview)
myscroll1.config(command=lb2.yview)

lb.insert(END,"Tea Rs.100")
lb.insert(END,"Coffee Rs.100")
lb.insert(END,"Pizza Rs.330")
lb.insert(END,"Puff Rs.120")
lb.insert(END,"Smoothee Rs.240")
lb.insert(END,"Shake Rs.280")
lb.insert(END,"Vada Pav Rs.120")
lb.insert(END,"Cold Coffee Rs.190")
lb.insert(END,"Mac n Cheese Rs.450")
lb.insert(END,"Idli Rs.120")
lb.insert(END,"Dosa Rs.190")
lb.insert(END,"Rice Rs.160")
lb.insert(END,"Noodles Rs.200")
lb.insert(END,"Fried Rice Rs.200")
lb.insert(END,"Dabeli Rs.120")
lb.insert(END,"Bhel Rs.120")
lb.insert(END,"Panipuri Rs.120")
lb.insert(END,"Fries Rs.160")
lb.insert(END,"Burger Rs.160")
lb.insert(END,"Cold Drink Rs.100")
lb.insert(END,"Lassi Rs.110")
lb.insert(END,"Sizzler Rs.640")
lb.insert(END,"Chaas Rs.100")

root.mainloop()