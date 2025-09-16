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
