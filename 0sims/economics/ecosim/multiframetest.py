try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

balance = 12.00

class MyBankApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.grid(row=1,column=1)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames = {}

        for F in (loginpage,registrationpage,dashboard,withdrawmoney,addmoney,done):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("loginpage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class loginpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="login page", font=controller.title_font)
        label.grid(row=0,column=2)

        ulabel = tk.Label(self, text="username", font=controller.title_font)
        ulabel.grid(row=1,column=0)

        username = tk.Entry(self)
        username.grid(row=1,column=1)

        pwlabel = tk.Label(self, text="password", font=controller.title_font)
        pwlabel.grid(row=2,column=0)
         
        pw = tk.Entry(self)
        pw.grid(row=2,column=1)

        submitfield =  tk.Button(self, text="submit",
                            command=lambda:self.checklogin(username=username,pw=pw,controller=controller))
        submitfield.grid(row=3,column=1)
    
    def checklogin(self,username,pw,controller):
        usernam = username.get()
        pw = pw.get()
        print("u" + usernam + " " + pw)
        controller.show_frame('dashboard')

class registrationpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        uname = tk.Entry()
        pw = tk.Entry()
        submitfield = tk.Button(self,text="submit",command=lambda:self.checkreg)
    def checkreg(self):
        controller.show_frame("dashboard")

class dashboard(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        label = tk.Label(self, text="dashboard", font=controller.title_font)
        label.grid(row=0,column=2)

        addmoneybu = tk.Button(self, text="addmoney",
                            command=lambda: controller.show_frame("addmoney"))
        button2 = tk.Button(self, text="withdraw money",
                            command=lambda: controller.show_frame("withdrawmoney"))
        addmoneybu.grid(row=1,column=1)
        button2.grid(row=1,column=2)

class withdrawmoney(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label1 = tk.Label(self, text="Withdraw Money Page ", font=controller.title_font)
        label1.grid(row=1,column=2)

        label2 = tk.Label(self, text="balance " + str(balance), font=controller.title_font)
        label2.grid(row=2,column=1)

        labelamounttowithdraw = tk.Label(self, text="amount to withdraw", font=controller.title_font)
        labelamounttowithdraw.grid(row=3,column=1)


        withdraw = tk.Entry(self)
        withdraw.grid(row=3,column=2)

        cancelbutton = tk.Button(self, text="cancel",
                           command=lambda: controller.show_frame("dashboard"))

        submitbutton = tk.Button(self, text="enter",
                           command=lambda:self.withdraw(controller=controller,withdraw=withdraw))
        cancelbutton.grid(row=4,column=2)

        submitbutton.grid(row=4,column=1)

    def withdraw(self,controller,withdraw):
        global balance
        amount = withdraw.get()
        balance = balance - float(amount)
        print(balance)
        controller.show_frame("done")

class addmoney(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Money Page ", font=controller.title_font)
        label.grid(row=0,column=2)
        balanceLabel = tk.Label(self, text="Balance " + str(balance), font=controller.title_font)
        balanceLabel.grid(row=1,column=2)
        amounttoadd = tk.Label(self, text="amount to add ", font=controller.title_font)
        amounttoadd.grid(row=2,column=0)


        addmoney = tk.Entry(self)
        addmoney.grid(row=2,column=1)

        enterbutton = tk.Button(self, text="enter",
                           command=lambda:self.addmoney(controller=controller,addmoney=addmoney,balance=balance))
        dashbutton = tk.Button(self, text="cancel ",
                           command=lambda: controller.show_frame("dashboard"))
        enterbutton.grid(row=3,column=1)

        dashbutton.grid(row=3,column=2)

    def addmoney(self,controller,addmoney,balance):
        amount = addmoney.get()
        balance = amount + balance
        controller.show_frame("done") 
    
class done(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        print(balance)
        label = tk.Label(self, text="You are done your Balance now is " + str(balance), font=controller.title_font)
        label.grid(row=1,column=2)
        button = tk.Button(self, text=" done",
                           command=lambda: controller.show_frame("login"))
        button.grid(row=1,column=1)

if __name__ == "__main__":
    app = MyBankApp()
    app.mainloop()