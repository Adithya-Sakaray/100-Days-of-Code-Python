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


def only_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated:
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


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    is_sold = db.Column(db.Boolean, nullable=False)


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
        log_user = result.scalar()
        # Email doesn't exist
        if not log_user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        # Password incorrect
        elif not check_password_hash(log_user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(log_user)
            return redirect(url_for('home'))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user email is already present in the database.
        result = db.session.execute(db.select(User).where(User.email == form.email.data))
        reg_user = result.scalar()
        if reg_user:
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
@only_authenticated
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

    return render_template("home.html", products=products_list)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/add_cart")
def add_to_cart():
    user_id = request.args.get("user_id")
    product_id = request.args.get("product_id")

    cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id, is_sold=False).first()

    if cart_item:
        # If the cart item already exists, update the quantity
        cart_item.quantity = (cart_item.quantity + 1)
        db.session.commit()
    else:
        # If the cart item doesn't exist, create a new one
        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=1,
            is_sold=False
        )

        db.session.add(cart_item)
        db.session.commit()

    return redirect(url_for("cart"))


@app.route("/remove_cart")
@only_authenticated
def remove_from_cart():
    cart_id = request.args.get("cart_id")

    cart_item = Cart.query.get(cart_id)

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for("cart"))


@app.route("/buy")
@only_authenticated
def buy():
    cart_id_param = request.args.get("cart_ids")
    cart_ids = cart_id_param.split(",")
    cart_ids.pop(-1)

    for cart_id in cart_ids:
        cart_item = Cart.query.get(int(cart_id))

        if cart_item:
            cart_item.is_sold = True
            db.session.commit()

    return redirect(url_for("cart"))


@app.route("/cart")
def cart():
    if current_user.is_authenticated:
        user_id = current_user.id
        user_cart = Cart.query.filter_by(user_id=user_id, is_sold=False).all()

        # Retrieve product details for each item in the cart
        cart_items = []
        total_price = 0

        for item in user_cart:
            product = Products.query.get(item.product_id)
            quantity = item.quantity
            subtotal = quantity * product.price
            total_price += subtotal

            cart_items.append({
                'product_name': product.product_name,
                'product_desc': product.description,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal,
                'img_url': product.img_url,
                'id': item.id
            })

        cart_ids = [x["id"] for x in cart_items]
        cart_str = ""
        for id in cart_ids:
            cart_str += str(id)
            cart_str += ","

    else:
        cart_items = []
        total_price = 0
        cart_str = ""

    return render_template("cart.html", current_user=current_user, cart_items=cart_items, total_price=total_price,
                           ids=cart_str)


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
@only_authenticated
def user():
    if current_user.is_authenticated:
        user_id = current_user.id
        user_cart = Cart.query.filter_by(user_id=user_id, is_sold=True).all()

        # Retrieve product details for each item in the cart
        order_items = []
        total_price = 0

        for item in user_cart:
            product = Products.query.get(item.product_id)
            quantity = item.quantity
            subtotal = quantity * product.price
            total_price += subtotal

            order_items.append({
                'product_name': product.product_name,
                'product_desc': product.description,
                'price': product.price,
                'quantity': quantity,
                'subtotal': subtotal,
                'img_url': product.img_url,
                'id': item.id
            })

    else:
        order_items = []
        total_price = 0
    return render_template("user.html", current_user=current_user, orders=order_items)


if __name__ == '__main__':
    app.run(debug=True)
