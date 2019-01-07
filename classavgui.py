from tkinter import*

root = Tk()

heading = Label(root, text="CLASS AVERAGE", font=("Helvetica", 20))
heading.grid(row=0,column=1)

classbutton = Button(root, text="Back", width=10, background='Yellow')
classbutton.grid(row=4, column=1)

title1= Label(root, text="My average: ")

title1.grid(row=1, column=0,sticky = "E")

title2= Label(root, text="Class overall average: ")

title2.grid(row=2, column=0,sticky = "E")

root.mainloop()
