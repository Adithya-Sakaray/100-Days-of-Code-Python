from flask import Flask
from random import randint

app = Flask(__name__)

rand_num = randint(0, 9)
print(rand_num)


@app.route("/")
def home_page():
    return '<h2>Guess a number between 0 and 9. Then enter it into </h2>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:user_number>")
def show_screen(user_number):
    if user_number == rand_num:
        return '<h2>You guessed it right!!</h2>' \
               '<img src="https://media.giphy.com/media/PaDop2n7PziNIfYpbu/giphy.gif">'
    else:
        return '<h2>You are wrong!!</h2>' \
               '<img src="https://media.giphy.com/media/6QxXEiJnnwOQPRnl0I/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
