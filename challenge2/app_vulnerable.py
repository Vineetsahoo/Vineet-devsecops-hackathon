from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)

    return "User fetched"


@app.route("/ping")
def ping():
    host = request.args.get("host")

    os.system(f"ping -c 1 {host}")

    return "Ping executed"


if __name__ == "__main__":
    app.run(debug=True)
