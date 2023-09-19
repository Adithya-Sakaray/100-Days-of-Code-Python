from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login", methods=['POST'])
def login_page():
    name = request.form.get('username')
    password = request.form.get('password')
    return render_template("login.html", username=name, password=password)

if __name__ == "__main__":
    app.run(debug=True)

