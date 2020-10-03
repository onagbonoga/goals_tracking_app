from flask import Flask, url_for, redirect, Blueprint,render_template,session
from werkzeug.security import generate_password_hash

from prol import db
from prol.user.forms import RegisterForm, LoginForm
from prol.user.models import User 

user_app = Blueprint('User',__name__)

@user_app.route('/register', methods=('GET','POST'))
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data)
		user = User(
			form.first_name.data,
			form.last_name.data,
			form.email.data,
			hashed_password
			)
		db.session.add(user)
		db.session.commit()
		
		user.query.filter_by(email=form.email.data).first()
		session['id'] = user.id
		session['first_name'] = user.first_name
		return redirect(url_for('User.home'))
	return render_template("register.html",form=form)

@user_app.route('/',methods=('GET','POST'))
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		session['id'] = user.id
		session['first_name'] = user.first_name
		return redirect(url_for('User.home'))
	return render_template('login.html',form=form)

@user_app.route('/home')
def home():
	#first_name = session['first_name']
	return render_template("index.html",first_name=session['first_name'])

@user_app.route('/logout')
def logout():
	session.pop('id')
	session.pop('first_name')
	return redirect(url_for('User.login'))
