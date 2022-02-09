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
    all_transactions = cur.execute("SELECT date, price, type FROM transactions ORDER BY date ASC")

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

    return render_template("transactions.html", all_transactions=all_transactions)


if __name__ == "__main__":
    app.run(debug=True)
