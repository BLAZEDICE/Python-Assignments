from tkinter import *
root=Tk()
root.geometry("700x700")

def validate():
    words=word_val.get()
    rev_word=words[::-1]
    Label(root,text=rev_word).place(x=120,y=55)

word_lab=Label(root,text="Enter a word :").place(x=10,y=10)
word_val=StringVar()
word_inp=Entry(root,textvariable=word_val).place(x=120,y=10)
valid_but=Button(root,text="Validate",command=validate,padx=120).place(x=120,y=90)

root.mainloop()