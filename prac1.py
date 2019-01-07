from tkinter import*


class Login():
    #to initialise upon a class, using this will run immediately. 
    def q1():
        
        #frame is the window
        w=Frame()
        w.pack(side="top", fill="both", expand=True)
        w.grid_rowconfigure(0,weight=1)
        w.grid_columnconfigure(0,weight=1)
        self.frames={}

        frame = Menu(container, self)

        self.frames[Menu]=frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

        def show_frame(self,cont):
            frame=self.frames[cont]
            frame.tkraise()

class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l=Label(self,text="Main Menu")
        l.pack(pady=10,padx=10)

root=Login()
root.mainloop()
        
##from tkinter import*
##
##
##class Login(tk.Tk):
##    #to initialise upon a class, using this will run immediately. 
##    def __init__(self, *args, **kwargs):
##        tk.Tk.__init__(self,*args, **kwargs)
##        #frame is the window
##        w=tk.Frame(self)
##        w.pack(side="top", fill="both", expand=True)
##        w.grid_rowconfigure(0,weight=1)
##        w.grid_columnconfigure(0,weight=1)
##        self.frames={}
##
##        frame = Menu(container, self)
##
##        self.frames[Menu]=frame
##
##        frame.grid(row=0, column=0, sticky="nsew")
##
##        self.show_frame(Menu)
##
##        def show_frame(self,cont):
##            frame=self.frames[cont]
##            frame.tkraise()
##
##class Menu(tk.Frame):
##
##    def __init__(self, parent, controller):
##        tk.Frame.__init__(self, parent)
##        l=Label(self,text="Main Menu")
##        l.pack(pady=10,padx=10)
##
##root=Login()
##root.mainloop()
##                
##         


