import os
from datetime import datetime
import sqlite3
from functools import wraps
from flask import Flask, g, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallback-secret-key-for-dev")
DATABASE = os.getenv("DATABASE_NAME", "atm.db")


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            account_number TEXT NOT NULL UNIQUE,
            pin TEXT NOT NULL,
            bank_name TEXT NOT NULL,
            dob TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            timestamp TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )
    conn.commit()

    user = cursor.execute(
        "SELECT id FROM users WHERE account_number = ?",
        ("12345678",),
    ).fetchone()
    if user is None:
        cursor.execute(
            """
            INSERT INTO users (name, account_number, pin, bank_name, dob, balance)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                "Aman Sharma",
                "12345678",
                "1234",
                "Campus Bank",
                "1999-05-12",
                15000.00,
            ),
        )
        conn.commit()
    conn.close()


@app.before_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        conn = get_db_connection()
        g.user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("login"))
        return view(**kwargs)

    return wrapped_view


def insert_transaction(user_id, transaction_type, amount, description=""):
    conn = get_db_connection()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn.execute(
        "INSERT INTO transactions (user_id, type, amount, timestamp, description) VALUES (?, ?, ?, ?, ?)",
        (user_id, transaction_type, amount, timestamp, description),
    )
    conn.commit()
    conn.close()


def get_transactions(user_id, limit=None):
    conn = get_db_connection()
    query = "SELECT * FROM transactions WHERE user_id = ? ORDER BY id DESC"
    if limit:
        query += " LIMIT ?"
        rows = conn.execute(query, (user_id, limit)).fetchall()
    else:
        rows = conn.execute(query, (user_id,)).fetchall()
    conn.close()
    return rows


def get_user_by_credentials(account_number, pin):
    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE account_number = ? AND pin = ?",
        (account_number, pin),
    ).fetchone()
    conn.close()
    return user


def update_balance(user_id, new_balance):
    conn = get_db_connection()
    conn.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        account_number = request.form.get("account_number", "").strip()
        pin = request.form.get("pin", "").strip()

        if not account_number or not pin:
            flash("Please enter both account number and PIN.", "error")
            return render_template("login.html")

        user = get_user_by_credentials(account_number, pin)
        if user is None:
            flash("Invalid account number or PIN. Try again.", "error")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user["id"]
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    transactions = get_transactions(g.user["id"], limit=3)
    return render_template("dashboard.html", transactions=transactions)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    if request.method == "POST":
        amount_text = request.form.get("amount", "0").strip()
        try:
            amount = float(amount_text)
        except ValueError:
            flash("Enter a valid numeric amount.", "error")
            return render_template("deposit.html")

        if amount <= 0:
            flash("The deposit amount must be greater than zero.", "error")
            return render_template("deposit.html")

        new_balance = g.user["balance"] + amount
        update_balance(g.user["id"], new_balance)
        insert_transaction(g.user["id"], "Deposit", amount, "Deposit money")
        flash(f"₹{amount:.2f} deposited successfully.", "success")
        return redirect(url_for("dashboard"))

    return render_template("deposit.html")


@app.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    if request.method == "POST":
        amount_text = request.form.get("amount", "0").strip()
        try:
            amount = float(amount_text)
        except ValueError:
            flash("Enter a valid numeric amount.", "error")
            return render_template("withdraw.html")

        if amount <= 0:
            flash("The withdrawal amount must be greater than zero.", "error")
            return render_template("withdraw.html")

        if amount > g.user["balance"]:
            flash("Insufficient balance for this withdrawal.", "error")
            return render_template("withdraw.html")

        new_balance = g.user["balance"] - amount
        update_balance(g.user["id"], new_balance)
        insert_transaction(g.user["id"], "Withdrawal", amount, "Withdraw money")
        flash(f"₹{amount:.2f} withdrawn successfully.", "success")
        return redirect(url_for("dashboard"))

    return render_template("withdraw.html")


@app.route("/balance")
@login_required
def balance():
    return render_template("balance.html")


@app.route("/history")
@login_required
def history():
    transactions = get_transactions(g.user["id"])
    return render_template("history.html", transactions=transactions)


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
