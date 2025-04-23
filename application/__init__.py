from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = 'SN}x}O>i};/SE?w(C2ovevOEJFad`C>Gx4m>roF>,g$,e?HW=1v4OeX26~w:"$c'


db = SQLAlchemy(app)

from application import routes

