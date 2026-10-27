# Hotel Management System

A small hotel booking management web app built with Python, Flask, and SQLite.

## Features
- Add guest bookings with room number and check-in/check-out dates
- View all saved bookings
- Delete bookings
- SQLite database is created automatically on first run
- Responsive, simple interface

## Tech stack
- Python 3.10+
- Flask
- SQLite (included with Python)

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

## Notes
This is an educational portfolio project, not a production hotel system. Before deployment, set a secure secret key, disable debug mode, add authentication and authorization, and strengthen booking/date validation.
