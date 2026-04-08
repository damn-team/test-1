

import os
import sqlite3
import pickle
import base64
import subprocess
from flask import Flask, request, render_template_string, redirect, session, send_file

app = Flask(__name__)


app.config['SECRET_KEY'] = "super-secret-key-12345"
a = 2

#bhai tera namm kya hai bc mc 
def get_db_connection():
    conn = sqlite3.connect('library.db')   # relative path — fragile
    return conn


def init_db():
    """Initialize the database with sample data."""
    conn = get_db_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS books (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            title    TEXT NOT NULL,
            author   TEXT NOT NULL,
            genre    TEXT,
            copies   INTEGER DEFAULT 1
        );
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,       -- [V12-related] stored as plain text
            role     TEXT DEFAULT 'user'
        );
        CREATE TABLE IF NOT EXISTS borrows (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id   INTEGER,
            book_id   INTEGER,
            due_date  TEXT
        );
        INSERT OR IGNORE INTO books (title, author, genre, copies)
        VALUES
            ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 3),
            ('Clean Code', 'Robert C. Martin', 'Technology', 2),
            ('1984', 'George Orwell', 'Dystopian', 5),
            ('Python Crash Course', 'Eric Matthes', 'Technology', 4),
            ('Dune', 'Frank Herbert', 'Sci-Fi', 2);
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES
            ('admin', 'admin123', 'admin'),
            ('alice', 'password', 'user'),
            ('bob',   'bob123',   'user');
    """)
    conn.commit()
    conn.close()




HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Management System</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        h1   { color: #333; }
        nav a { margin-right: 15px; color: #0066cc; text-decoration: none; }
        nav a:hover { text-decoration: underline; }
        .card { background: white; padding: 20px; border-radius: 8px; margin-top: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>📚 Library Management System</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/books">All Books</a>
        <a href="/search">Search</a>
        <a href="/login">Login</a>
        <a href="/borrow">Borrow</a>
        <a href="/admin/dashboard">Admin</a>
    </nav>
    <div class="card">
        <h2>Welcome to the Library</h2>
        <p>Browse our collection, search for books, and manage your borrowings.</p>
    </div>
</body>
</html>
"""

BOOKS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Books</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
        th { background: #0066cc; color: white; }
        tr:nth-child(even) { background: #f9f9f9; }
    </style>
</head>
<body>
    <h1>📖 All Books</h1>
    <a href="/">← Back Home</a>
    <br><br>
    <table>
        <tr><th>ID</th><th>Title</th><th>Author</th><th>Genre</th><th>Copies</th></tr>
        {% for book in books %}
        <tr>
            <td>{{ book[0] }}</td>
            <td>{{ book[1] }}</td>
            <td>{{ book[2] }}</td>
            <td>{{ book[3] }}</td>
            <td>{{ book[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


SEARCH_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Search Books</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
        input, button { padding: 8px 12px; font-size: 14px; }
        button { background: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .result { background: white; padding: 15px; margin-top: 20px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>🔍 Search Books</h1>
    <a href="/">← Back Home</a>
    <br><br>
    <form method="GET" action="/search">
        <input type="text" name="title" placeholder="Enter book title..." value="{{ query }}">
        <button type="submit">Search</button>
    </form>
    {% if search_result %}
    <div class="result">
        <!-- [V9] Unescaped output — XSS possible -->
        <p>{{ search_result | safe }}</p>
    </div>
    {% endif %}
</body>
</html>
"""

LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; display: flex; justify-content: center; }
        .box { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); width: 320px; }
        input { width: 100%; padding: 8px; margin: 8px 0 16px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 100%; padding: 10px; background: #0066cc; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 15px; }
        .error { color: red; font-size: 13px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>🔐 Login</h2>
        {% if error %}<p class="error">{{ error }}</p>{% endif %}
        <form method="POST" action="/login">
            <label>Username</label>
            <input type="text" name="username" required>
            <label>Password</label>
            <input type="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
"""




@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)


@app.route('/books')
def list_books():
    conn = get_db_connection()
    books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return render_template_string(BOOKS_TEMPLATE, books=books)


# ======================== STARTUP ========================

if __name__ == "__main__":
    init_db()

    app.run(host='0.0.0.0', port=5000, debug=True)
