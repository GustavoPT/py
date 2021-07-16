from flask import Flask, render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
admin = Admin(app)

class Product:
    pass

# class Project(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(80))
#     videourl = db.Column(db.String(80))
#     description = db.Column(db.String(80))
#     category = db.Column(db.String(80))
#     tag = db.Column(db.String(80))
#     giturl = db.Column(db.String(80))
#     demourl = db.Column(db.String(80))
#     imageurl = db.Column(db.String(80))

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()