from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserInputForm(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                          choices = [('income', 'Income'), ('expense', 'Expense')])
    
    category = SelectField('Category', validators=[DataRequired()],
                           choices=[
                               ('Salary', 'Salary'),
                               ('Freelance', 'Freelance'),
                               ('Investments', 'Investments'),
                               ('Gifts', 'Gifts'),
                               ('Refunds', 'Refunds'),
                               ('Side Business', 'Side Business'),
                               ('Bonus', 'Bonus'),
                               ('Other Income', 'Other Income'),
                               ('Rent', 'Rent'),
                               ('Groceries', 'Groceries'),
                               ('Utilities', 'Utilities'),
                               ('Transportation', 'Transportation'),
                               ('Dining Out', 'Dining Out'),
                               ('Entertainment', 'Entertainment'),
                               ('Shopping', 'Shopping'),
                               ('Healthcare', 'Healthcare'),
                               ('Education', 'Education'),
                               ('Travel', 'Travel'),
                               ('Insurance', 'Insurance'),
                               ('Subscriptions', 'Subscriptions'),
                           ])
    
    amount = IntegerField('Amount', validators=[DataRequired()])

    submit = SubmitField("Add Data")