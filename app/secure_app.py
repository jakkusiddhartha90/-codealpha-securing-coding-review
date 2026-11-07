"""Safer local Flask demo for the secure-coding review."""
from flask import Flask, abort, request, render_template_string
import sqlite3

app = Flask(__name__)

# Keep the demo database small and local. Parameterized SQL is used below.
def get_item(item_id: int):
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, label TEXT)")
        connection.execute("INSERT INTO items (id, label) VALUES (?, ?)", (1, "demo item"))
        return connection.execute(
            "SELECT label FROM items WHERE id = ?", (item_id,)
        ).fetchone()
    finally:
        connection.close()

@app.get("/")
def home():
    name = request.args.get("name", "student")
    # Jinja auto-escapes values in HTML templates by default.
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)

@app.get("/lookup")
def lookup():
    raw_id = request.args.get("id", "1")
    try:
        item_id = int(raw_id)
    except (TypeError, ValueError):
        abort(400, description="id must be an integer")
    if item_id < 1:
        abort(400, description="id must be a positive integer")
    result = get_item(item_id)
    return {"result": result[0] if result else None}

@app.errorhandler(400)
def bad_request(error):
    return {"error": error.description}, 400

if __name__ == "__main__":
    # Local-only development server; debug remains disabled.
    app.run(host="127.0.0.1", port=5000, debug=False)
