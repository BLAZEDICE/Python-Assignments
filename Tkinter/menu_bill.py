from tkinter import *
root=Tk()
root.geometry("700x500")
W=Label(root,text="Menu",font="50").pack()

Checkbutton1=IntVar()
Checkbutton2=IntVar()  
Checkbutton3=IntVar()
Checkbutton4=IntVar()

def calculate():
    pizza=Checkbutton1.get()
    dosa=Checkbutton2.get()
    maggi=Checkbutton3.get()
    cold_drink=Checkbutton4.get()
    bill=0
    if (pizza):
        bill+=200
    if (dosa):
        bill+=150
    if (maggi):
        bill+=100
    if (cold_drink):
        bill+=30
    l1=Label(root,text=f"Your total bill is {bill}").pack()
    
    

Button1=Checkbutton(root,text="Pizza Rs200",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,width=10,command=calculate).pack()
Button2=Checkbutton(root,text="Dosa Rs.150",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,width=10,command=calculate).pack()
Button3=Checkbutton(root,text="Maggi Rs.100",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,width=10,command=calculate).pack()
Button4=Checkbutton(root,text="Cold Drink Rs.30",variable=Checkbutton4,onvalue=1,offvalue=0,height=2,width=12,command=calculate).pack()

# bill=Checkbutton1.get()+Checkbutton2.get()+Checkbutton3.get()+Checkbutton4.get()
# calc_btn=Button(root,text='Calculate',command=calculate).pack()
# l1=Label(root,text=f"Your total bill is {bill}").pack()
print(Button1)

root.mainloop()