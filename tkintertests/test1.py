from tkinter import * 
class cell:
    pass


class blood:
    pass 

class heart:
    pass 

#print("blood flow speed" + str(2))

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master 

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH,expand=1)
        quitButton = Button(self,text="Quit",command=self.client_exit)
        quitButton.place(x=0,y=0)

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()