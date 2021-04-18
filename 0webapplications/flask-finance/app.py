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

@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()