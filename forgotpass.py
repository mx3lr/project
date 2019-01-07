from tkinter import*

root= Tk()

title = Label(root, text="Forgot password:", font=("Helvetica", 20))
title.grid(row=0,column=0)  #pack puts it into the window

subheading = Label(root, text="If you are unsure about your login details, please enter your email address below. A confirmation email will be sent to you with your new password.", font=("Helvetica", 10))
subheading.grid(row=1,column=0)

back = Button(root, text="Back", width=10, background='Yellow')
back.grid(row=6, column=2)

email=Label(root, text='Email address:')
e1=Entry(root)
email.grid(row=0,column=1,sticky = "E")
e1.grid(row=0,column=2)

np=Label(root, text='New password:')
np1=Entry(root)
np.grid(row=1,column=1,sticky = "E")
np1.grid(row=1,column=2)

c=Label(root, text='Confirm new password:')
c1=Entry(root)
c.grid(row=3,column=1,sticky = "E")
c1.grid(row=3,column=2)


loginbutton=Button(root, text='Reset password', background='Purple',fg ="White")
loginbutton.grid(row=4, column=2)


root.mainloop()

