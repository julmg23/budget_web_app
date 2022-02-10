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
    # Configure sqlite3 Database
    con = sqlite3.connect('transactions.db')

    # This returns the single values from a row, allowing them to be added later
    con.row_factory = lambda cursor, row: row[0]
    cur = con.cursor()

    # Retrieve Income and Expenses
    income = cur.execute("SELECT price FROM transactions WHERE type = 'Income'").fetchall()
    expenses = cur.execute("SELECT price FROM transactions WHERE type = 'Expense'").fetchall()

    sum_income = sum(income)
    sum_expenses = sum(expenses)

    # Net worth is income minus expenses
    net_worth = sum_income - sum_expenses

    return render_template("index.html", net_worth=net_worth, usd=usd)


@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    """Show transactions page"""

    # Configure sqlite3 Database
    con = sqlite3.connect('transactions.db')
    cur = con.cursor()

    # Retrieve all transactions and display on page
    all_transactions = cur.execute("SELECT date, price, type FROM transactions ORDER BY date DESC")

    if request.method == "POST":
        # Get date
        date = request.form.get("date")

        # Get price
        price = request.form.get("price")

        # Get type
        type = request.form.get("type")

        # Insert into table
        cur.execute("INSERT INTO transactions (date, price, type) VALUES (?, ?, ?)", (date, price, type))

        con.commit()

        return redirect("/transactions")

    return render_template("transactions.html", all_transactions=all_transactions, usd=usd)


if __name__ == "__main__":
    app.run(debug=True)
