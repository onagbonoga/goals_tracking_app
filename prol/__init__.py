import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
#print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from prol.user.views import user_app 
from prol.goals.views import goals_app

app.register_blueprint(user_app)
app.register_blueprint(goals_app)