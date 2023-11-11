from flask import Flask, abort, render_template, redirect, url_for, flash, request
from forms import *
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_ckeditor import CKEditor
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
import os

# app configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_URI", 'sqlite:///shop.db')

# package linking with the app
Bootstrap5(app)
ckeditor = CKEditor(app)
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function


# table definitions
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(400), nullable=False)


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        # Email doesn't exist
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        if form.password.data == form.confirm_password.data:
            hash_and_salted_password = generate_password_hash(
                form.password.data,
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                email=form.email.data,
                name=form.name.data,
                password=hash_and_salted_password,
            )
            db.session.add(new_user)
            db.session.commit()
            # This line will authenticate the user with Flask-Login
            login_user(new_user)
            return redirect(url_for("home"))
        else:
            flash("Both the passwords did not match!!")
            return redirect(url_for("register"))
    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/', methods=["POST", "GET"])
def home():
    products_list = db.session.execute(db.select(Products)).scalars().all()
    length = len(products_list)
    if length > 5:
        products_list = products_list[:5]

    if request.method == "POST":
        search_query = request.form.get("search")
        search_results = []
        for item in products_list:
            if search_query.lower() in item.product_name.lower():
                search_results.append(item)

        return render_template("search.html", query=search_query, results=search_results)


    return render_template("home.html", current_user=current_user, products=products_list)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/cart")
def cart():
    return render_template("cart.html", current_user=current_user)


@app.route("/products")
def products():
    products_list = db.session.execute(db.select(Products)).scalars().all()
    return render_template("products.html", current_user=current_user, products=products_list)


@app.route("/add", methods=["POST", "GET"])
@admin_only
def products_form():
    form = NewProductForm()
    if form.validate_on_submit():
        new_product = Products(
            product_name=form.product_name.data,
            price=form.price.data,
            description=form.description.data,
            img_url=form.img_url.data
        )
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for("products"))
    return render_template("products_form.html", form=form)


@app.route("/edit-product", methods=["POST", "GET"])
@admin_only
def edit_product():
    prod_id = request.args.get("product_id")
    product = db.get_or_404(Products, prod_id)
    edit_form = NewProductForm(
        product_name=product.product_name,
        price=product.price,
        img_url=product.img_url,
        description=product.description,
    )

    if edit_form.validate_on_submit():
        product.product_name = edit_form.product_name.data
        product.price = edit_form.price.data
        product.img_url = edit_form.img_url.data
        product.description = edit_form.description.data
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("products_form.html", current_user=current_user, form=edit_form)


@app.route("/search", methods=["POST", "GET"])
def search():
    query = request.args.get("query")
    return render_template("search.html", current_user=current_user, query=query)


@app.route("/user")
def user():
    return render_template("user.html", current_user=current_user)


if __name__ == '__main__':
    app.run()
