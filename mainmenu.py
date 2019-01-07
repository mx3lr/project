from tkinter import*

root=Tk()

tFrame=Frame(root)
tFrame.grid()

bFrame=Frame(root)
bFrame.grid(columnspan=2)

assbutton = Button(tFrame, text="ASSESSMENTS", width=20, fg ="Purple")
assbutton.grid(row=1, column=3)

achbutton = Button(tFrame, text="ACHIEVEMENTS", width=20, fg ="Purple")
achbutton.grid(row=2, column=3)

classbutton = Button(tFrame, text="CLASS AVERAGE", width=20, fg ="Purple")
classbutton.grid(row=3, column=3)

teachbutton = Button(tFrame, text="TEACHERS COMMENTS", width=20, fg ="Purple")
teachbutton.grid(row=4, column=3)

root.mainloop()

