from application import app, db
from flask import render_template, flash, redirect, url_for
from application.forms import UserInputForm
from application.models import IncomeExpenses

@app.route("/")
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template("index.html", title="Home Page", entries=entries)

@app.route("/add", methods=["GET", "POST"])
def add_expenses():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(
            type=form.type.data,
            category=form.category.data,
            amount=form.amount.data
        )
        db.session.add(entry)
        db.session.commit()
        flash("Entry added successfully!", "success")
        return redirect(url_for("index"))

    return render_template('add.html', title='add', form=form )

@app.route("/delete/<int:entry_id>")
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully!", "success")
    return redirect(url_for("index"))

