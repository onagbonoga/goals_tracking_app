from flask import Flask, Blueprint, url_for, render_template,request, redirect,session
import json

from prol import db
from prol.goals.models import Goal, GoalMod
from prol.goals.forms import AddGoalForm
goals_app = Blueprint('Goals', __name__)

@goals_app.route('/view_goals',methods =("GET","POST"))
def view_goals():
	
	if request.method == "POST":
		if 'save low' in request.form:
			allGoals = Goal.query.filter_by(user_id = session['id'], priority="low")
		elif 'save medium' in request.form:
			allGoals = Goal.query.filter_by(user_id = session['id'], priority="medium")
		elif 'save high' in request.form:
			allGoals = Goal.query.filter_by(user_id = session['id'], priority="high")
		allGoalsD = deSerialize(allGoals)
		#x = request.form.getlist('something')
		#return f"{x}"
		#keylist = []
		i = -1 #for indexing
		for eachGoal in allGoalsD: #checking each object in all goals 
			i = i + 1
			for key in eachGoal.todo.keys(): #checking each key in each todo list
				keyName = "\""+key+"\""
				keyName = key
				response = request.form.get(keyName)
				#return f"{keyName}: {response}"
				if response != None:

					eachGoal.todo[key] = True
					allGoals[i].todo = json.dumps(eachGoal.todo)

						
				else:
					eachGoal.todo[key] = False
					allGoals[i].todo = json.dumps(eachGoal.todo)
					
			
			db.session.commit()

	low = Goal.query.filter_by(user_id = session['id'], priority = "low")
	low = deSerialize(low)
	medium = Goal.query.filter_by(user_id = session['id'], priority = "medium")
	medium = deSerialize(medium)
	high = Goal.query.filter_by(user_id = session['id'], priority = "high")
	high = deSerialize(high)
	#return f"{low[0].todo}"
	return render_template('view_goals.html',low = low, medium=medium, high = high)

@goals_app.route('/add_goals',methods =("GET","POST"))
def add_goals():
	form = AddGoalForm()
	
	if form.validate_on_submit():
		todoItemsList = request.form.getlist("todoItemF")
		user_id = session['id']
		todo = json.dumps(parseTodo(todoItemsList))
		#todo = pickle.dumps(todo)
		newGoal = Goal(
			form.goal.data,
			form.priority.data,
			todo,
			user_id
			)
		db.session.add(newGoal)
		db.session.commit()
		return redirect(url_for('Goals.view_goals'))
	return render_template('add_goals.html', form = form)

@goals_app.route('/view_goals_cards', methods = ("GET","POST"))
def view_goals_cards():
	low = Goal.query.filter_by(user_id = session['id'], priority = "low")
	low = deSerialize(low)
	medium = Goal.query.filter_by(user_id = session['id'], priority = "medium")
	medium = deSerialize(medium)
	high = Goal.query.filter_by(user_id = session['id'], priority = "high")
	high = deSerialize(high)

	return render_template("view_goals_cards.html", low = low, medium = medium, high = high, count = [1,2,3,4])

def parseTodo(todo):
	#input to this function will be a string with enter to seperate items
	#this function will store these items as a dict 
	result = {}
	for currentItem in todo:
		result[currentItem] = False
	return result

def deSerialize(goalList):
	result = [] #storing the todo items as a list instead of a json string
	for eachGoal in goalList:
		newTodo = json.loads(eachGoal.todo)
		result.append(GoalMod(eachGoal.goal, #goal mod is a class i created to make it easy to extract the data on the template
				eachGoal.priority,
				newTodo))

	return result






