
from flask import Flask, flash, redirect, render_template, request
import sqlite3



# Configure application
app = Flask(__name__)


# Convert to USD function
def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


@app.route("/")
def index():
    """Show application page"""
    return render_template("index.html")


@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    """Show transactions page"""

    # Configure sqlite3 Database
    con = sqlite3.connect('transactions.db')
    cur = con.cursor()

    # Retrieve all transactions and display on page
    all_transactions = cur.execute("SELECT date, price, type FROM transactions ORDER BY date")

    if request.method == "POST":


        cur.execute("INSERT INTO transactions (date, price, type) VALUES (?, ?, ?)", date, price, type)

        return redirect("/transactions")

    return render_template("transactions.html")


if __name__ == "__main__":
    app.run(debug=True)