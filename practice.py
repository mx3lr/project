from tkinter import*

root= Tk()

name=Label(root, text='USERNAME:')
n1=Entry(root)
name.grid(row=0,column=1)
n1.grid(row=0,column=2)

password=Label(root, text='PASSWORD:')
p1=Entry(root)
password.grid(row=1,column=1)
p1.grid(row=1,column=2)

root.mainloop()
