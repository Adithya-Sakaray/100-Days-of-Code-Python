import random
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, FloatField, SelectField, SubmitField
from wtforms.validators import InputRequired, URL
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[InputRequired()])
    map_url = URLField("Location URL", validators=[InputRequired(), URL()])
    img_url = URLField("Image URL", validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    seats = StringField('Seats', validators=[InputRequired()])
    has_toilet = SelectField('Toilet', validators=[InputRequired()], choices=[(1, "Yes"), (2, "No")])
    has_wifi = SelectField('Wi-Fi', validators=[InputRequired()], choices=[(1, "Yes"), (2, "No")])
    has_sockets = SelectField('Sockets', validators=[InputRequired()], choices=[(1, "Yes"), (2, "No")])
    can_take_calls = SelectField('Calls', validators=[InputRequired()], choices=[(1, "Yes"), (2, "No")])
    coffee_price = FloatField("Coffee Price", validators=[InputRequired()])
    submit = SubmitField("Submit")


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    list_of_cafes = []
    for cafes in all_cafes:
        list_of_cafes.append(cafes.to_dict())

    print(list_of_cafes)
    return render_template("home.html", list_of_cafes=list_of_cafes)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        data = form.data
        new_cafe = Cafe(
            name=data["name"],
            map_url=data["map_url"],
            img_url=data["img_url"],
            location=data["location"],
            has_sockets=bool(data["has_sockets"]),
            has_toilet=bool(data["has_toilet"]),
            has_wifi=bool(data["has_wifi"]),
            can_take_calls=bool(data["can_take_calls"]),
            seats=data["seats"],
            coffee_price=f"£{data['coffee_price']}",
        )
        db.session.add(new_cafe)
        db.session.commit()
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run()
