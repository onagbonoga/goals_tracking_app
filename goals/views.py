from flask import Flask, Blueprint, url_for, render_template, redirect,session

from app import db
from goals.models import Goal
from goals.forms import AddGoalForm
goals_app = Blueprint('Goals', __name__)

@goals_app.route('/view_goals')
def view_goals():
	goals = Goal.query.filter_by(user_id = session['id'])
	#return f"{goals[0].todo}"
	return render_template('view_goals.html',goals=goals)

@goals_app.route('/add_goals',methods =("GET","POST"))
def add_goals():
	form = AddGoalForm()
	
	if form.validate_on_submit():
		user_id = session['id']
		todo = parseTodo(form.todo.data)
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

def parseTodo(todo):
	#input to this function will be a string with enter to seperate items
	#this function will store these items as a dict 

	result = {}
	currentItem = ""
	for letter in todo:
		if letter =='|':
			result[currentItem] = False
			currentItem = ""
		else:
			currentItem = currentItem + letter
	result[currentItem] = False
	return result




