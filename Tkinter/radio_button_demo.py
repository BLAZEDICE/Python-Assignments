from tkinter import *
window=Tk()
window.title('Window')
window.geometry('500x300')

var=StringVar()
l=Label(window,bg='white',width=20,text='')
l.pack()

def print_selection():
    l.config(text="You have selected "+var.get())

r1=Radiobutton(window,text="Option A",variable=var,value='A',command=print_selection).pack()
r2=Radiobutton(window,text="Option B",variable=var,value='B',command=print_selection).pack()
r3=Radiobutton(window,text="Option C",variable=var,value='C',command=print_selection).pack()
window.configure(background="gray")

window.mainloop()