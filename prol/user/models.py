from prol import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	email = db.Column(db.String(80))
	password = db.Column(db.String(128))
	goals = db.relationship('Goal', backref = 'user',lazy = 'dynamic')

	def __init__(self,first_name,last_name,email,password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

	def __repr__(self):
		return f"User: {self.first_name} {self.last_name}"
