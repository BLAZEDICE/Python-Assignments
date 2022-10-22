from tkinter import *

root=Tk()
root.geometry("500x500")
scroll=Scrollbar(root)
scroll.pack(fill=Y,side=RIGHT)

lb=Listbox(root,yscrollcommand=scroll.set)
lb.pack()


for i in range(30):
    lb.insert(END,"Number "+str(i))
lb.pack()

scroll.config(command=lb.yview)
root.mainloop()