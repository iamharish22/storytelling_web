from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user data (for demo)
users = {"admin": "1234"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            return redirect(url_for("home"))
        else:
            error = "Invalid username or password"
    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if username in users:
            return render_template("register.html", error="Username already exists")
        users[username] = password
        return redirect(url_for("login"))

    return render_template("register.html", error=None)

if __name__ == "__main__":
    app.run(debug=True)
