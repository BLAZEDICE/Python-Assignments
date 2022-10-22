from tkinter import *
pane=Tk()
bt=Button(pane,text="Click Me!")
bt.pack(fill=Y,expand=True)

bt2=Button(pane,text="Click Me Too!")
bt2.pack(fill=X,expand=True) 
pane.mainloop()