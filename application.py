import os
from flask import Flask, flash, redirect, render_template, request

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

if __name__ == "__main__":
    app.run(debug=True)