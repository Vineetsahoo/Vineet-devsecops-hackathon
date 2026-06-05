from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)


@app.route("/user")
def get_user():
    username = request.args.get("username")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ?"

    cursor.execute(query, (username,))

    return "User fetched securely"


@app.route("/ping")
def ping():
    host = request.args.get("host")

    try:
        result = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout

    except subprocess.CalledProcessError:
        return "Ping failed"


if __name__ == "__main__":
    app.run(debug=False)
