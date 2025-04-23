from application import db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), default='income', nullable=False)
    category = db.Column(db.String(50), nullable=False, default='rent')
    date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow) 
    amount = db.Column(db.Float, nullable=False)

    def __str__(self):
        return f"{self.type} - {self.category} - {self.date} - {self.amount}"
