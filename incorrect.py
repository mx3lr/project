from tkinter import*

root= Tk()

title = Label(root, text="CHEMVISION", font=("Helvetica", 30), fg ="Purple")
title.grid(row=0,column=0)  #pack puts it into the window

subheading = Label(root, text="The Chemistry revision app", font=("Helvetica", 10))
subheading.grid(row=1,column=0)

name=Label(root, text='USERNAME:')
n1=Entry(root, width=20)
name.grid(row=0,column=1)
n1.grid(row=0,column=2)

password=Label(root, text='PASSWORD:')
p1=Entry(root, show="*", width=20)
password.grid(row=1,column=1)
p1.grid(row=1,column=2)

rem=Checkbutton(root, text="Remember password")
rem.grid(row=2, column=2)

incorrect=Label(root, text="Your details are incorrect. Please try again or click ‘Forgot your password?’ below", fg ="Red")
incorrect.grid(row=3, column=2)

loginbutton=Button(root, text='LOG IN', background='Purple',fg ="White")
loginbutton.grid(row=4, column=2)

forgot=Label(root, text="FORGOT YOUR PASSWORD?")
forgot.grid(row=5, column=2)

create=Label(root, text="DON'T HAVE A LOGIN? REGISTER HERE", fg="Purple")
create.grid(row=7, column=2)

root.mainloop()
