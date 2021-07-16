try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from flask import Flask, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import time 
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aa09@localhost/bankeco-sim"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    price = db.Column(db.Float)
    name = db.Column(db.String(100))
    isService = db.Column(db.Boolean)

class Seller(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(500))
    transactions = db.relationship('Transaction',backref='seller')

class Transaction(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # one to one
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False) 
    #
    amount = db.Column(db.Float)
    # one to one
    card_id = db.Column(db.Integer,db.ForeignKey("card.id"),nullable=False) 
    #one to one
    seller_id = db.Column(db.Integer,db.ForeignKey("seller.id"),nullable=False) 

    date = db.Column(db.Integer)
    
class Account(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    #use 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    
    balance = db.Column(db.Float)

class Card(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number  = db.Column(db.Integer)
    year    = db.Column(db.Integer)
    month   = db.Column(db.Integer)
    backcode = db.Column(db.Integer)
    image = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),unique=True)
    transactions = db.relationship('Transaction',backref='card')

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    physical_address = db.Column(db.String(128))
    cards = db.relationship('Card',backref='user')
    transactions = db.relationship('Transaction',backref='user')
    accounts = db.relationship('Account',backref='user')

    def __str__(self):
        return self.name

class Bank:
    def __init__(self,reserve = 0.00,users = None,activeUsers=None):
        self.reserve = reserve 
        self.users = users 
        self.activeUsers = activeUsers
        self.transactions = transactions 

    def getTransactions(self,User):
        transactions = Transaction.query.all()

    def getLoan(self,amount):
        loan = self.money - amount 
        self.money = self.money - amount
        return loan 

    def withDrawMoney(self,amount):
        self.money = self.money - amount
        return self.money 

    def addMoney(self,amount):
        self.money = self.money + amount
        print("added amoutn" + amount)

    def login(self,user):
        User.query.filter_by(name=user.name)

        pass 
    def logout(self,user):
        pass 
    # def add
    def register(self,user):
        if user.name is not '':
            if user.password is not '':
                u = User(name=name,password=password)
                db.session.add(u)
                db.session.commit()
        pass 

    def addUser(self,user):
        self.user = user
        self.activeUsers.append(user)
        print("added user " + user.name)

    def removeUser(self,user):
        self.activeUsers
        for i in range(0,len(activeUsers)):
            if(activeUsers[i].name == user.name):
                self.activeUsers.pop(i)
            else:
                print("user with the name " + user.name + " could not be found \n")
        
balance = 12.00
sessionuser = User(name="test")
sac = Account(user_id=sessionuser.id,balance=1.00)
sessionuser.accounts.append(sac) 
  
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

        errorlabel = tk.Label(self, text="", font=controller.title_font)
        errorlabel.grid(row=0,column=3)

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
    
        register =  tk.Button(self, text="register",
                            command=lambda:controller.show_frame('registrationpage'))
        register.grid(row=3,column=2)
    def checklogin(self,username,pw,controller):
        usernam = username.get()
        pw = pw.get()
        print("u" + usernam + " " + pw)
        User.query.filter_by()
        user = User.query.filter(User.name.like(usernam),User.password.like(pw)).first()
        if(user):
        #    login_user(user)
           global sessionuser
           sessionuser = user
           controller.show_frame('dashboard')
        else:
            self.errorlabel.text ="c"

class registrationpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        label = tk.Label(self, text="registration page", font=controller.title_font)
        label.grid(row=0,column=2)

        errorlabel = tk.Label(self, text="", font=controller.title_font)
        errorlabel.grid(row=0,column=3)

        ulabel = tk.Label(self, text="username", font=controller.title_font)
        ulabel.grid(row=1,column=0)

        username = tk.Entry(self)
        username.grid(row=1,column=1)

        pwlabel = tk.Label(self, text="password", font=controller.title_font)
        pwlabel.grid(row=2,column=0)
         
        pw = tk.Entry(self)
        pw.grid(row=2,column=1)

        submitfield =  tk.Button(self, text="submit",
                            command=lambda:self.checkreg(username=username,pw=pw))
        submitfield.grid(row=3,column=1)
    
        register =  tk.Button(self, text="login",
                            command=lambda:controller.show_frame('loginpage'))
        register.grid(row=3,column=2)

    def checkreg(self,username,pw):
        username = username.get()
        pw = pw.get()
        print("username" + username)
        print("pw" + pw)

        user = User.query.filter(User.name.like(username),User.password.like(pw)).first()
             
        if(user):
           self.errorlabel.text ="user already exists"
           print("already")
        else:
            u2 = User(name=username,password=pw)
            a1 = Account(balance=0.00,user_id=u2.id)
            u2.accounts.append(a1)
            db.session.add(u2)
            db.session.commit()
            db.session.add(a1)
            db.session.commit()
            global sessionuser 
            sessionuser = u2
            # login_user(u2)
            self.controller.show_frame('dashboard')

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

        logout = tk.Button(self, text="logout",
                            command=lambda: self.logout(controller=controller))
        
        logout.grid(row=1,column=3)
    def logout(self,controller):
        sessionuser = None 
        controller.show_frame("loginpage")

class withdrawmoney(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label1 = tk.Label(self, text="Withdraw Money Page ", font=controller.title_font)
        label1.grid(row=1,column=2)
        global sessionuser
        balance = sessionuser.accounts[0].balance
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
        global sessionuser
        amount = withdraw.get()
        print(amount)
        balance = sessionuser.accounts[0].balance
        print(balance)
        sessionuser.accounts[0].balance = balance - float(amount)
        print(sessionuser.accounts[0].balance)
        user = User.query.filter_by(id=sessionuser.id)
        user.accounts[0].balance = balance - float(amount)
        db.session.commit()
        sessionuser = user
        controller.show_frame("done")

class addmoney(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        balance = sessionuser.accounts[0].balance

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
        global sessionuser
        amount = addmoney.get()
        print(amount)
        balance = sessionuser.accounts[0].balance
        print(balance)
        sessionuser.accounts[0].balance = balance + float(amount)
        print(sessionuser.accounts[0].balance)
        user = User.query.filter_by(id=sessionuser.id)
        user.accounts[0].balance = balance + float(amount)
        db.session.commit()
        sessionuser = user
        controller.show_frame("done") 
    
class done(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        print(balance)
        label = tk.Label(self, text="You are done your Balance now is " + str(sessionuser.accounts[0].balance), font=controller.title_font)
        label.grid(row=1,column=2)
        button = tk.Button(self, text=" done",
                           command=lambda:self.done)
        button.grid(row=1,column=1)
    def done(self):
        logout_user()
        self.controller.show_frame("login")

if __name__ == "__main__":
    app = MyBankApp()
    app.mainloop()