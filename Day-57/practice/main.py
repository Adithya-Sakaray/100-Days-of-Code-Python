from flask import Flask
from flask import render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    curr_year = str(date.today().year)
    print(curr_year)
    return render_template("index.html", year=curr_year)


@app.route("/guess/<name>")
def guess_page(name):
    age_endpoint = "https://api.agify.io/"
    age_params = {
        "name": name
    }
    gen_endpoint = "https://api.genderize.io/"
    gen_params = {
        "name": name
    }
    age_response = requests.get(url=age_endpoint, params=age_params)
    gen_response = requests.get(url=gen_endpoint, params=gen_params)
    age = age_response.json()["age"]
    gender = gen_response.json()["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)