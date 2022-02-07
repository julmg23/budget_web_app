import os
from flask import Flask, flash, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# Configure SQLAlchemy Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
db = SQLAlchemy(app)

class Transaction(db.model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Smallmoney, nullable=False)
    type = db.Column(db.Text, nullable=False)


# Convert to USD function
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

@app.route("/")
def index():
    """Show application page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)