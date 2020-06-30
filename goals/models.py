from app import db
#from sqlalchemy.ext.mutable import MutableDict


class Goal(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	goal = db.Column(db.Text) 
	priority = db.Column(db.String(80))
	todo = db.Column(db.Text)
	#todo = db.Column(db.PickleType)
	#todo = db.Column(db.JsonEncodedDict)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __init__(self, goal,priority,todo,user_id):
		self.goal = goal
		self.priority = priority
		self.todo = todo
		self.user_id = user_id


	def __repr__(self):
		return f"{self.goal}"


class GoalMod():
	def __init__(self,goal,priority,todo):
		self.goal = goal
		self.priority = priority
		self.todo = todo




