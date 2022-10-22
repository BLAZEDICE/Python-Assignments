from tkinter import *
w=Tk()
w.geometry("500x400")
w.configure(background="lightgreen")

favlist=["cricket","baseball","hockey"]
alllist=["Neflix","Instagram","Twitter"]

def ls1():
    selected=[]
    for i in lb1.curselection():
        c=lb1.get(i)
        selected.append(c)
    print(selected)

    for i,j in zip(selected,range(len(selected))):
        lb2.insert(END,i)
        lb1.delete(j)
l1=Label(w,text="Favourite List :",font=("Satisfy",20),justify=CENTER,background="lightgreen")
l1.grid(row=0,column=0)

l2=Label(w,text="All List :",font=("Satisfy",20),fg="white",justify=CENTER,background="lightgreen")
l2.grid(row=0,column=1)

lb1=Listbox(w,width=16,height=8,fg="maroon",font=("New Times Roman",16),background="silver",
            selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)
lb1.grid(row=1,column=3,padx=4,pady=55,rowspan=4)


lb2=Listbox(w,width=16,height=8,fg="maroon",font=("New Times Roman",16),background="silver",
            selectmode="multiple",selectbackground="lightgrey",selectforeground="black",justify=CENTER)
lb2.grid(row=1,column=3,padx=4,pady=55,rowspan=4)



LtoR_addAll=Button(text=">>",width=100,height=5,justify=CENTER,font="Satisfy 9")
LtoR_addAll.grid(row=1,column=1,padx=15,pady=2,ipadx=2)
w.mainloop()


