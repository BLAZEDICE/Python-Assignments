from tkinter import *

root=Tk()
root.geometry("500x500")

def getCourseList():
    selected_courses=[]
    curSelected=listSample.curselection()
    for i in curSelected:
        c=listSample.get(i)
        selected_courses.append(c)
    print(selected_courses)
    

courses=Label(text="Select Courses").pack()
courses_list=['Software Development','Animation','Itims','Digital Design']
listSample=Listbox(root,width=70,height=30,fg="red",font=("Arial 28"),selectmode="multiple")
for i in range(len(courses_list)):
    listSample.insert(END,courses_list[i])    
btn=Button(text="Get Courses",command=getCourseList)
btn.pack()
listSample.pack()
root.mainloop()

# listSample.insert(2,"Pizza")
# listSample.insert(0,"Pizza 2")
# listSample.insert(1,"Pizza 3")
listSample.pack()
root.mainloop()