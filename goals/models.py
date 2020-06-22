from app import db

class Goal(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	goal = db.Column(db.Text) 
	priority = db.Column(db.String(80))
	todo = db.Column(db.Text)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __init__(self, goal,priority,todo,user_id):
		self.goal = goal
		self.priority = priority
		self.todo = todo
		self.user_id = user_id


	def __repr__(self):
		return f"{self.goal}"
