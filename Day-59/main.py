import smtplib
from article_data import all_posts
from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
OWN_EMAIL = "guystrange656@gmail.com"
OWN_PASSWORD = "aezdyhxnjfqphruj"


@app.route("/")
def home_page():
    return render_template("index.html", posts=all_posts, num_posts=len(all_posts))


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/posts/<int:id>")
def post_page(id):
    post = all_posts[id - 1]
    image = "https://images.unsplash.com/photo-1542435503-956c469947f6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80"
    return render_template("post.html", post=post, image=image)


@app.route("/contact", methods=["POST", "GET"])
def contact_page():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact_success.html")
    else:
        return render_template("contact.html", msg_sent=False)


@app.route("/add", methods=["GET", "POST"])
def add_page():
    if request.method == "POST":
        data = request.form
        send = {
            "id": len(all_posts)+1,
            "body": data["body"],
            "date": data["date"],
            "title": data["title"],
            "author": data["author"],
            "subtitle": data["subtitle"]
        }
        all_posts.append(send)
        print(send)
        return render_template("thankyou.html")
    return render_template("add.html")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(from_addr=OWN_EMAIL, to_addrs=email, msg=email_message)


if __name__ == "__main__":
    app.run(debug=True)
