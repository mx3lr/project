from tkinter import*

root = Tk()

heading = Label(root, text="ASSESSMENT", font=("Helvetica", 20))
heading.grid(row=0,column=1)

assbutton = Button(root, text="Back", width=10, background='Yellow')
assbutton.grid(row=4, column=1)

title1= Label(root, text="Current tasks: ")

title1.grid(row=1, column=0,sticky = "E")

title2= Label(root, text="Due this week: ")

title2.grid(row=2, column=0,sticky = "E")

title3= Label(root, text="Due later: ")

title3.grid(row=3, column=0,sticky = "E")

title4= Label(root, text="Progress: ")

title4.grid(row=4, column=0,sticky = "E")


root.mainloop()
