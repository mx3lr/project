from tkinter import *
import time

#For my stopwatch I got help from the link referenced below:
#https://www.raspberrypi.org/forums/viewtopic.php?t=220614

class StopWatch(Frame):                                                                  
    def __init__(self, parent=None, **kwargs): #none defines no value in the parent argument       
        Frame.__init__(self, parent, **kwargs)
        self.start = 0.0        
        self.elapsed= 0.0
        self.running = 0
        self.timestr = StringVar()               
        self.Label()

    def Label(self):  #creates the time label                       
        label= Label(self, textvariable=self.timestr)
        self.Time(self.elapsed)
        label.pack(fill=X)                    
    
    def new(self): 
        self.elapsed= time.time() - self.start
        self.Time(self.elapsed)
        self.timer = self.after(60, self.new)
    
    def Time(self, elap): #sets time string
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        miliseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliseconds))
        
    def Start(self):  #function starts the stopwatch                                                   
        if not self.running:            
            self.start = time.time() - self.elapsed
            self.new()
            self.running = 1        
    
    def Stop(self):  #function stops, for the user finishes/exits the set of questions                                 
        if self.running:
            self.after_cancel(self.timer)            
            self.elapsed = time.time() - self.start    
            self.Time(self.elapsed)
            self.running = 0
    
    def Reset(self): #resets the stopwatch, for when the user starts a new set of questions                                
        self.start = time.time()         
        self.elapsed = 0.0    
        self.Time(self.elapsed)
        
        
def main(): #GUI for this function, displaying the timer, the start button, stop and reset button.
    root = Tk()
    watch = StopWatch(root)
    watch.pack(side=TOP)
    
    Button(root, text='Start', command=watch.Start).pack(side=LEFT)
    Button(root, text='Stop', command=watch.Stop).pack(side=LEFT)
    Button(root, text='Reset', command=watch.Reset).pack(side=LEFT)
    
    root.mainloop()

if __name__ == '__main__':
    main()
