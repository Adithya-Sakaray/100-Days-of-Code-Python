from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config['SECRET_KEY'] = 'XXXXXXXXXXXXXXXX'
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap5(app)


class TaskForm(FlaskForm):
    task_name = StringField("Task", validators=[InputRequired()])
    due_date = DateField("Due Date", validators=[InputRequired()])
    submit = SubmitField("Submit")


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(250), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        req_id = request.args.get("id")
        print(req_id)
        task = db.session.execute(db.select(Tasks).filter_by(id=req_id)).scalar_one()
        task.completed = bool(1)
        db.session.commit()
        redirect(url_for("home"))

    pending_tasks = db.session.execute(db.select(Tasks).filter_by(completed=0)).scalars().all()
    today_date = datetime.now()
    return render_template("home.html", tasks=pending_tasks, today_date=today_date)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        data = form.data
        new_task = Tasks(
            task_name=data["task_name"],
            due_date=data["due_date"],
            completed=bool(0)
        )
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html", form=form)


@app.route("/completed")
def completed():
    completed_tasks = db.session.execute(db.select(Tasks).filter_by(completed=1)).scalars().all()
    today_date = datetime.now()
    return render_template("completed.html", tasks=completed_tasks, today_date=today_date)


if __name__ == '__main__':
    app.run()
