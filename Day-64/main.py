from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ.get("movie_api")
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)


class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    movie_name = StringField("Movie Name")
    submit = SubmitField("Add")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=["GET", "POST"])
def update():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    if form.validate_on_submit():
        movie = Movies(
            id=data["id"],
            title=data["title"],
            year=data["release_date"][:4],
            description=data["overview"],
            rating=form.rating.data,
            ranking=1,
            review=form.review.data,
            img_url=f"https://image.tmdb.org/t/p/w500{data['backdrop_path']}"
        )
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=data, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.session.get(Movies, movie_id)
    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        return redirect(url_for("select", query=form.movie_name.data))

    return render_template("add.html", form=form)


@app.route("/select")
def select():
    url = "https://api.themoviedb.org/3/search/movie"
    para = {
        "query": request.args.get("query"),
        "api_key": API_KEY
    }
    response = requests.get(url=url, params=para)
    response = response.json()

    all_movies = response["results"]
    print(all_movies)

    return render_template("select.html", movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
