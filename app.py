from enum import unique
from flask import Flask, render_template,request
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


db = SQLAlchemy(app)



# data for the html template to draw from
table_headings = ("Sale Price","Buy Price","flip price")
scraper_data = ()


@app.route("/")
def hello_world(name=None):
    return render_template('SMA.html', name=name, headings=table_headings, data=scraper_data)

@app.route("/", methods=['POST'])
def getvalue():
    HTML_Info = request.form['data_bridge']
    

#@app.route("/register", methods=['GET','POST'])
#def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)

#@app.route("/login")
#def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)