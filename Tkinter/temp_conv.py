from tkinter import *
root=Tk()
root.geometry("500x300")

def convert():
    getCelc=celc_val.get()
    Label(root,text=f"{(getCelc * 9.0/5.0) + 32.0}").place(x=200,y=100)


celc_val=DoubleVar()

celc_inp=Entry(root,textvariable=celc_val)
celc_inp.place(x=200,y=20)
c_lab=Label(root,text="C")
c_lab.place(x=470,y=20)

f_lab=Label(root,text="F")
f_lab.place(x=470,y=100)

f_lab=Label(root,text="is equal to")
f_lab.place(x=0,y=100)

conv_but=Button(root,text="Convert",command=convert)
conv_but.place(x=430,y=270)

root.mainloop()