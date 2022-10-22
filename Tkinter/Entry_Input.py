import tkinter as tk
root=tk.Tk()
root.geometry("700x500")
name_var=tk.StringVar()
passwd_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=passwd_var.get()
    # print("The name is :"+name)
    # print("The password is :"+password)
    label_name=tk.Label(root,text=name).pack()
    label_passwd=tk.Label(root,text=password).pack()
    name_var.set("")
    passwd_var.set("")


name_label=tk.Label(root,text="Username",font=('Arial',10,'bold')).pack()
name_entry=tk.Entry(root,textvariable=name_var,font=('Arial',10,'bold')).pack()
passwd_label=tk.Label(root,text="Password",font=('Arial',10,'bold')).pack()
passwd_entry=tk.Entry(root,textvariable=passwd_var,font=('Arial',10,'bold'),show='*').pack()
sub_btn=tk.Button(root,text='Submit',command=submit).pack()

root.mainloop()