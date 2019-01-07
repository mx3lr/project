from tkinter import*

root= Tk()

subheading = Label(root, text="Details Form", font=("Helvetica", 20))
subheading.grid(row=0,column=0)

back = Button(root, text="Back", width=10, background='Yellow')
back.grid(row=6, column=2)

newname=Label(root, text='Name:')
n1=Entry(root)
newname.grid(row=0,column=1,sticky = "E")
n1.grid(row=0,column=2)

sn=Label(root, text='Surename:')
sn1=Entry(root)
sn.grid(row=1,column=1,sticky = "E")
sn1.grid(row=1,column=2)

dob=Label(root, text='Date of Birth:dd/mm/yyyy')
d1=Entry(root)
dob.grid(row=2,column=1,sticky = "E")
d1.grid(row=2,column=2)

year=Label(root, text='Class/Year:')
y1=Entry(root)
year.grid(row=3,column=1,sticky = "E")
y1.grid(row=3,column=2)


loginbutton=Button(root, text='CONFIRM', background='Purple',fg ="White")
loginbutton.grid(row=4, column=2)


root.mainloop()
