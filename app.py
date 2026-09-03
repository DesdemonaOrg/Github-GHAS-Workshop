from flask import Flask, request, jsonify
import subprocess
import sqlite3
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="GHAS workshop API", endpoints=["/hello", "/search", "/run"])

@app.get("/hello")
def hello():
    name = request.args.get("name", "world")
    return jsonify(message=f"Hello, {name}!")

@app.get("/search")
def search():
    # Intentionally vulnerable: SQL query built with string concatenation.
    name = request.args.get("name", "")
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE users (name TEXT)")
    connection.execute("INSERT INTO users VALUES ('alice')")
    connection.execute("INSERT INTO users VALUES ('bob')")
    query = "SELECT name FROM users WHERE name = '" + name + "'"
    rows = connection.execute(query).fetchall()
    return jsonify(users=[row[0] for row in rows])

@app.get("/run")
def run_command():
    allowed_commands = {
        "hello": ["echo", "hello"],
        "date": ["date"],
        "whoami": ["whoami"],
    }
    action = request.args.get("action", "hello")
    if action not in allowed_commands:
        return jsonify(error="Invalid action", allowed=list(allowed_commands.keys())), 400

    result = subprocess.run(allowed_commands[action], capture_output=True, text=True)
    return jsonify(output=result.stdout, error=result.stderr)

@app.get("/eval")
def evaluate():
    # Intentionally vulnerable custom CodeQL target.
    expression = request.args.get("expression", "1 + 1")
    result = eval(expression)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run()
