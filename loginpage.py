import tkinter as tk

class ChemVision(tk.Tk):
    #to initialise upon a class, using this will run immediately. 
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self,*args, **kwargs)
        #frame is the window
        container=tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={}

        frame = Login(container, self)

        self.frames[Login]=frame

        frame.grid(row=0, column=0, sticky="nesw")

        self.show_frame(Login)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = tk.Label(self, text="CHEMVISION", font=("Helvetica", 30), fg ="Purple")
        title.grid(row=0,column=0)  #pack puts it into the window

#pady=10, padx=10.. adding padding into code.


        subheading = tk.Label(self, text="The Chemistry revision app", font=("Helvetica", 10))
        subheading.grid(row=1,column=0)
        name=tk.Label(self, text='USERNAME:')
        n1=tk.Entry(self, width=20)
        name.grid(row=0,column=1)
        n1.grid(row=0,column=2)

        password=tk.Label(self, text='PASSWORD:')
        p1=tk.Entry(self, show="*", width=20)
        password.grid(row=1,column=1)
        p1.grid(row=1,column=2)

        rem=tk.Checkbutton(self, text="Remember password")
        rem.grid(row=2, column=2)

        loginbutton=tk.Button(self, text='LOG IN', background='Purple',fg ="White")
        loginbutton.grid(row=3, column=2)

app=ChemVision()
app.mainloop()


##import sqlite3 as sql
##
##aaaaa sql.connect(name of database)
