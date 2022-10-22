from tkinter import *
root=Tk()
root.geometry("700x500")
W=Label(root,text="Gujarat University",font="50").pack()



Checkbutton1=IntVar()
Checkbutton2=IntVar()  
Checkbutton3=IntVar()  


def submit():
    tut=Checkbutton1.get()
    stud=Checkbutton2.get()
    cours=Checkbutton2.get()
    # print("The name is :"+name)
    # print("The password is :"+password)
    print("hy",tut)
    print("stud",stud)
    if(tut==0):
        tut_name=Label(root,text="Tutorial").pack()
    if(stud==0):
        stud_name=Label(root,text="Student").pack()
    if(cours==0):
        cours_name=Label(root,text="Courses").pack()
    

Button1=Checkbutton(root,text="Tutorial",variable=Checkbutton1,onvalue=1,offvalue=0,height=2,width=10).pack()
Button2=Checkbutton(root,text="Student",variable=Checkbutton2,onvalue=1,offvalue=0,height=2,width=10).pack()
Button3=Checkbutton(root,text="Courses",variable=Checkbutton3,onvalue=1,offvalue=0,height=2,width=10).pack()
sub_btn=Button(root,text='Submit',command=submit).pack()

root.mainloop()