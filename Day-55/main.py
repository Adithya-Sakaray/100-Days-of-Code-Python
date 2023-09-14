from flask import Flask
from decorators import *
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/bye")
@make_bold
@make_italics
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<string:name>/1")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
