from flask import Flask, abort, render_template, redirect, url_for, flash, request, make_response
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def home():
    dark_mode = True
    if request.method == "POST":
        dark_mode != dark_mode
        return render_template("index.html", is_dark=dark_mode)
    return render_template("index.html", is_dark=dark_mode)






if __name__ == "__main__":
    app.run(debug=True)

