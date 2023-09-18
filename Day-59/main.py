from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(url=url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts, num_posts=len(all_posts))

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/posts/<int:id>")
def post_page(id):
    blog_url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
    response = requests.get(url=blog_url)
    post = response.json()[id - 1]
    image = post['image_url']
    return render_template("post.html", post=post, image=image)

if __name__ == "__main__":
    app.run(debug=True)