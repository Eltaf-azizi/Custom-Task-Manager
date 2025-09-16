from flask import render_template, redirect, url_for, request
from . import db
from .models import Task, Category
from datetime import datetime
from flask import current_app as app


@app.route("/")
def index():
    tasks = Task.query.order_by(Task.deadline).all()
    return render_template("index.html", tasks=tasks)


@app.route("/add-task", methods=["GET", "POST"])
def add_task():
    categories = Category.query.all()
    if request.method == "POST":
        title = request.form["title"]
        description = request.form.get("description")
        deadline = request.form.get("deadline")
        category_id = request.form.get("category")

        task = Task(
            title=title,
            description=description,
            deadline=datetime.strptime(deadline, "%Y-%m-%d") if deadline else None,
            category_id=category_id if category_id else None
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("add_task.html", categories=categories)


@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = Category.query.all()
