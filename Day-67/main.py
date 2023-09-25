import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CREATE A FORM

class NewBlogForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author_name = StringField("Your name", validators=[DataRequired()])
    img_url = URLField("Blog Image URL", validators=[DataRequired()])
    blog_content = CKEditorField('Blog Content')
    submit = SubmitField("Submit")


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/post')
def show_post():
    post_id = request.args.get("post_id")
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = NewBlogForm()

    if request.method == "POST":
        date = datetime.datetime.now()
        date_str = f"{date.strftime('%d')} {date.strftime('%B')}, {date.year}"
        print(date_str)
        blog = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=date_str,
            body=form.blog_content.data,
            author=form.author_name.data,
            img_url=form.img_url.data
        )

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for("get_all_posts"))

    return render_template("make-post.html", form=form, title="New Post")



@app.route("/edit-post/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    post = db.session.get(BlogPost, id)
    edit_form = NewBlogForm(
        title=post.title,
        subtitle=post.subtitle,
        author_name=post.author,
        img_url=post.img_url,
        blog_content=post.body
    )
    if request.method == "POST":
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author_name.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.blog_content.data
        db.session.commit()

        return  redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=edit_form, title="Edit Post")



@app.route("/delete/<int:id>")
def delete_post(id):
    post = db.session.get(BlogPost, id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
