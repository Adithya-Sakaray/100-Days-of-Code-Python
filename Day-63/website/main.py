from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)




@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        data = request.form
        book = db.session.get(Books, data["id"])
        book.rating = data["new_rating"]
        db.session.commit()
    books = Books.query.all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        data = request.form
        book = Books(
            title=data["book_name"],
            author=data["book_author"],
            rating=data["rating"]
        )
        db.session.add(book)
        db.session.commit()
    return render_template("add.html")

@app.route("/edit")
def edit():
    book_id = request.args.get('id')
    data = db.session.get(Books, book_id)
    return render_template("edit.html", book=data)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = db.session.get(Books, book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

