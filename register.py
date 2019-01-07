from tkinter import*

root= Tk()

title = Label(root, text="Registration Form:", font=("Helvetica", 20))
title.grid(row=0,column=0)  #pack puts it into the window

subheading = Label(root, text="Password must contain at least 8 characters including uppercase and lowercase letters, numbers and a special character.", font=("Helvetica", 10))
subheading.grid(row=1,column=0)

back = Button(root, text="Back", width=10, background='Yellow')
back.grid(row=6, column=2)

newn=Label(root, text='Username:')
n1=Entry(root)
newn.grid(row=0,column=1,sticky = "E")
n1.grid(row=0,column=2)

email=Label(root, text='Email:')
e1=Entry(root)
email.grid(row=1,column=1,sticky = "E")
e1.grid(row=1,column=2)

p=Label(root, text='Password:')
p1=Entry(root)
p.grid(row=2,column=1,sticky = "E")
p1.grid(row=2,column=2)

c=Label(root, text='Confirm password:')
c1=Entry(root)
c.grid(row=3,column=1,sticky = "E")
c1.grid(row=3,column=2)


loginbutton=Button(root, text='Register', background='Purple',fg ="White")
loginbutton.grid(row=4, column=2)


root.mainloop()
