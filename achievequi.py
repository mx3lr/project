from tkinter import*

root = Tk()

heading = Label(root, text="ACHIEVEMENTS", font=("Helvetica", 20))
heading.grid(row=0,column=1)

achbutton = Button(root, text="Back", width=10, background='Yellow')
achbutton.grid(row=4, column=1)

title1= Label(root, text="Highest score achieved: ")

title1.grid(row=1, column=0,sticky = "E")

title2= Label(root, text="Started questions: ")

title2.grid(row=2, column=0,sticky = "E")

title3= Label(root, text="Questions finished: ")

title3.grid(row=3, column=0,sticky = "E")


root.mainloop()
