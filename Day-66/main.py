import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
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


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(result)

    return jsonify(
        cafe={
            "id":random_cafe.id,
            "name": random_cafe.name,
            "map_url": random_cafe.map_url,
            "img_url": random_cafe.img_url,
            "location": random_cafe.location,
            "seats": random_cafe.seats,
            "has_toilet": random_cafe.has_toilet,
            "has_wifi": random_cafe.has_wifi,
            "has_sockets": random_cafe.has_sockets,
            "can_take_calls": random_cafe.can_take_calls,
            "coffee_price": random_cafe.coffee_price,
        }

    )


@app.route("/all")
def get_all_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    list_of_cafes = []
    for cafes in all_cafes:
        list_of_cafes.append(cafes.to_dict())
    return jsonify(cafes=list_of_cafes)


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafes = db.session.execute(db.select(Cafe).filter_by(location=location)).scalars().all()

    if len(cafes) > 0:
        return jsonify(
            cafes=[cafe.to_dict() for cafe in cafes]
        )
    else:
        return jsonify(
            error={
                "Not found": "Sorry we don't have a cafe at that location"
            }
        )



@app.route("/add", methods=["POST", "GET"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:id>")
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(response={"failure": "No cafe found with the given id."})



@app.route("/report-closed/<int:id>")
def report_closed(id):
    api_key = request.args.get("api-key")

    if api_key == "TopSecretApiKey":
        cafe = db.session.get(Cafe, id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "The mentioned cafe is deleted from the database."})
        else:
            return jsonify(response={"failure": "No cafe found with the given id."})

    else:
        return jsonify(response={"failure": "You dont have permission to do that, please check the api key"})



if __name__ == '__main__':
    app.run(debug=True)
