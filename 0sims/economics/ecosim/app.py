from flask import Flask, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import time 
import tkinter 
import tkinter as tk

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aa09@localhost/bankeco-sim"
db = SQLAlchemy(app)

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

class User(db.Model):
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
        self.money = self.money - 
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
            if(activeUsers[i].name == user.name)
                self.activeUsers.pop(i)
            else:
                print("user with the name " + user.name + " could not be found \n")
        
    
w= tkinter.Tk()


u = User(name="gustavo")
p = Product(price=12.00)
s = Seller(name="rah")
b = Bank(reserve=0.00)

button = tk.Button(w, text='Stop', width=25, command=w.destroy)
button.grid(row=1,column=1)

tk.Label(w, text='').grid(row=0,column=2)

registerButton = tk.Button(w,text="register",width=25,command=b.register)
loginButton = tk.Button(w,text="register",width=25,command=b.login)
addMoneyButton = tk.Button(w,text="register",width=25,command=b.addMoney)
withDrawMoneyButton = tk.Button(w,text="register",width=25,command=b.withDrawMoney)


listofusers = ttk.Scrollbar(w)



#make someone sell something 
# give a list of sellers 
# make someone buy something 
# list of users 
# buy a product 
# from them 
# make a new transaction 
# if statement 
# run 

# scrollable frame make each user 
#


# row = 0 col = 0 row = 1 col = 1 
# row = 2 col = 2 
# row = 3 col = 3
w.mainloop()
