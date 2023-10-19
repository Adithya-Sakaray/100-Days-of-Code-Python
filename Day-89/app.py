from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("home.html")


@app.route("/add", methods=["POST", "GET"])
def add():
    return render_template("add.html")


@app.route("/completed")
def completed():
    return render_template("completed.html")


if __name__ == '__main__':
    app.run()
