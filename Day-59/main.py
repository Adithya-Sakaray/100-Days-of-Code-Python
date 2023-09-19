import smtplib

from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
OWN_EMAIL = "guystrange656@gmail.com"
OWN_PASSWORD = "aezdyhxnjfqphruj"


@app.route("/")
def home_page():
    url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(url=url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts, num_posts=len(all_posts))


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/posts/<int:id>")
def post_page(id):
    blog_url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(url=blog_url)
    post = response.json()[id - 1]
    image = post['image_url']
    return render_template("post.html", post=post, image=image)


@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact_success.html")
    else:
        return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=email, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
