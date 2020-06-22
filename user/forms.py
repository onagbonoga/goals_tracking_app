from flask_wtf import FlaskForm
from wtforms import validators,StringField,PasswordField,ValidationError,SubmitField
from werkzeug.security import check_password_hash
from wtforms.fields.html5 import EmailField
import email_validator
from user.models import User 


class RegisterForm(FlaskForm):
	first_name = StringField('First Name', [validators.InputRequired()])
	last_name = StringField('Last Name', [validators.InputRequired()])
	email = StringField('Email', [validators.InputRequired(), validators.Email()])
	password = PasswordField('New password', [validators.InputRequired(),validators.length(min=4,max=80)])
	confirm_password = PasswordField('Repeat Password',[validators.EqualTo('password',message='Passwords must match')])
	submit = SubmitField("Register")
	
	def validate_email(self,email): #checking if someone already resistered with the same email
		author = User.query.filter_by(email=email.data).first()
		if author is not None: #if an author already exists
			raise ValidationError('Email already registered')

class LoginForm(FlaskForm):
	email = StringField('Email', [validators.InputRequired(), validators.Email()])
	password = PasswordField('Password', [validators.InputRequired(),validators.length(min=4,max=80)])
	submit = SubmitField("Login")

	def validate(self): #this is a global validator so we dont need to pass in any attribute
		rv = FlaskForm.validate(self) #checking if it passes the basic validation
		if not rv:
			return False

		user = User.query.filter_by(email=self.email.data).first()

		if user:
			if not check_password_hash(user.password, self.password.data):
				self.password.errors.append('Incorrect email of password')
				return False

			return True
		else:
			self.password.errors.append('Incorrect email of password')
			return False

