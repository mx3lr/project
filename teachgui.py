from tkinter import*

root = Tk()

heading = Label(root, text="TEACHERS COMMENT", font=("Helvetica", 20))
heading.grid(row=0,column=1)

teachbutton = Button(root, text="Back", width=10, background='Yellow')
teachbutton.grid(row=4, column=1)

title1= Label(root, text="What went well: ")

title1.grid(row=1, column=0,sticky = "E")

title2= Label(root, text="What could you do next time to improve: ")

title2.grid(row=2, column=0,sticky = "E")

root.mainloop()
