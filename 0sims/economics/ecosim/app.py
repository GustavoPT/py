from flask import Flask, render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import time 
import tkinter 
import tkinter as tk
#  from tkinter import ttk 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aa09@localhost/bankeco-sim"
db = SQLAlchemy(app)

class Country:
    pass 

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

class state:
    #neightbors 
    # location 
    # lat
    #longitude 
    pass 

class Bank:


    def __init__(self,money,reserve,accounts):
        self.reserve = reserve 
        self.money = money
        self.accounts = accounts 

    def getLoan(self,amount):
        loan = self.money - amount 
        self.money = self.money - amount
        return loan 

    def getMoney(self):
        return self.money

    def addMoney(self,amount):
        self.money = self.money + amount
        print("added amoutn" + amount)

    # def add
    
w= tkinter.Tk()


# b = Bank()
u = User()
p = Product()
s = Seller()

button = tk.Button(w, text='Stop', width=25, command=w.destroy)
button.grid(row=1,column=1)

tk.Label(w, text='Economics Simulation').grid(row=0,column=2)
tk.Label(w, text='Press To Add Mo').grid(row=0)



yscrollbar = ttk.Scrollbar(w)



tk.Label(w, text='Population').grid(row=0)
tk.Label(w, text='').grid(row=0)
tk.Label(w, text='one day pass ').grid(row=0)
tk.Label(w, text='one year ').grid(row=0)
tk.Label(w, text='one month').grid(row=0)

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
