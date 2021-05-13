from flask_sqlalchemy import SQLAlchemy
import time 

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

def register():
    pass

class company:
    pass 


# day 
# cook 
# eat 
# 

# fast 

class Bank:
    # services 
    # take out loans 
    # make deposits 
    # make 
    pass 

def passageOfTime():
    start_time = time.monotic()
    print('seconds: ', time.monotonic() - start_time)
    pass 
while True:
    print("Economics the simulation")
    print("the time of day today is ")
    print("the stock market is")
    print("show graph with matplitlib of the stock market ")
    print("A  " )
    print("make a passage of time ")
    print("the passage of time is 1 hour 1 day 1 year")
    print("print the population out and the ritches of each")
    print("population")
    print("the upper class middle class higher class")


# if the user is getting poorere then 
# go to the bank and take out a loan from the 
# bank take out l;p