from flask_wtf import FlaskForm
from wtforms import BooleanField, validators,SelectField,TextAreaField,StringField,PasswordField,ValidationError,SubmitField
from werkzeug.security import check_password_hash
from wtforms.fields.html5 import EmailField
import email_validator
from prol.goals.models import Goal 

class AddGoalForm(FlaskForm):
	goal = StringField('Goal', [validators.InputRequired()])
	priority = SelectField("Priority:",
		choices=[('low','low'),('medium','medium'),('high','high')])
	todo = TextAreaField('To do')
	submit = SubmitField("Add goal")

def validate():
	if FlaskForm.validate(self):
		return True
	return False


