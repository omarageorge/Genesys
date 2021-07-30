from flask import Flask, render_template, redirect, url_for, session, request, logging
from flask.helpers import flash
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

from sqlhelpers import *
from forms import *


app = Flask(__name__)


# MySQL database connection config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'omara'
app.config['MYSQL_PASSWORD'] = 'quantum1'
app.config['MYSQL_DB'] = 'genesys'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


def log_in_user(username):
    pass


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    users = Table('users', 'name', 'email', 'username', 'password')
    
    if request.method ==  'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
    
        if isnewuser(username):
            password = sha256_crypt.encrypt(form.password.data)
            users.insert(name, email, username, password)
            log_in_user(username)
            return redirect(url_for('dashboard'))
        else:
            flash('User already exists', 'danger') 
            return redirect(url_for('register'))          
    
    return render_template('register.html', form=form)



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True, port=3000)