from flask import Flask, abort, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegisterForm
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@app.route('/')
def home():  # put application's code here
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/search")
def search():
    return render_template("search.html")




if __name__ == '__main__':
    app.run()
