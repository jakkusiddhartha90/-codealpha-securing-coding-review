"""INTENTIONALLY INSECURE training example. Inspect only; never deploy.

This file demonstrates common mistakes for the secure-coding review:
- string-built SQL query (SQL injection risk)
- rendering user input as HTML (XSS risk)
- debug mode enabled
"""
from flask import Flask, request, Response
import sqlite3

app = Flask(__name__)

@app.get("/")
def home():
    name = request.args.get("name", "student")
    # UNSAFE: user input is concatenated into HTML without escaping.
    return Response("<h1>Hello " + name + "</h1>", mimetype="text/html")

@app.get("/lookup")
def lookup():
    item_id = request.args.get("id", "1")
    # UNSAFE: concatenating untrusted input into SQL.
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE items (id INTEGER, label TEXT)")
    connection.execute("INSERT INTO items VALUES (1, 'demo item')")
    query = "SELECT label FROM items WHERE id = " + item_id
    try:
        result = connection.execute(query).fetchone()
        return {"result": result[0] if result else None}
    finally:
        connection.close()

if __name__ == "__main__":
    # UNSAFE: debug mode should not be enabled in production.
    app.run(host="127.0.0.1", port=5001, debug=True)
