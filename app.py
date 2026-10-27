from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-for-production"
DB_PATH = Path(__file__).with_name("hotel.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                guest_name TEXT NOT NULL,
                room_number TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT NOT NULL
            )
        """)

@app.route("/")
def index():
    with get_db() as db:
        bookings = db.execute("SELECT * FROM bookings ORDER BY id DESC").fetchall()
    return render_template("index.html", bookings=bookings)

@app.route("/book", methods=["POST"])
def book():
    guest_name = request.form.get("guest_name", "").strip()
    room_number = request.form.get("room_number", "").strip()
    check_in = request.form.get("check_in", "").strip()
    check_out = request.form.get("check_out", "").strip()
    if not all([guest_name, room_number, check_in, check_out]):
        flash("Please complete every field.", "error")
        return redirect(url_for("index"))
    if check_out < check_in:
        flash("Check-out date must be on or after check-in date.", "error")
        return redirect(url_for("index"))
    with get_db() as db:
        db.execute(
            "INSERT INTO bookings (guest_name, room_number, check_in, check_out) VALUES (?, ?, ?, ?)",
            (guest_name, room_number, check_in, check_out),
        )
    flash("Booking added successfully.", "success")
    return redirect(url_for("index"))

@app.route("/delete/<int:booking_id>", methods=["POST"])
def delete_booking(booking_id):
    with get_db() as db:
        db.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))
    flash("Booking deleted.", "success")
    return redirect(url_for("index"))

init_db()

if __name__ == "__main__":
    app.run(debug=True)
