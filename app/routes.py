from flask import (
    current_app, render_template, redirect, url_for, flash, request, abort
)
from . import db
from .models import Task, Category
from .forms import TaskForm, CategoryForm
from flask import Blueprint
from datetime import datetime

from flask import current_app as app  # using factory pattern's app context

# We will register routes directly; since we imported routes in __init__ under app context,
# using app.route directly works.


@app.route("/")
def index():
    # filter by category or show all
    category_id = request.args.get("category", type=int)
    q = request.args.get("q", "", type=str).strip()
    if category_id:
        tasks_query = Task.query.filter_by(category_id=category_id)
    else:
        tasks_query = Task.query

    if q:
        tasks_query = tasks_query.filter(Task.title.ilike(f"%{q}%"))

    tasks = tasks_query.order_by(Task.deadline.asc().nulls_last(), Task.created_at.desc()).all()
    categories = Category.query.order_by(Category.name).all()
    return render_template("index.html", tasks=tasks, categories=categories, selected_category=category_id, q=q)



@app.route("/task/add", methods=["GET", "POST"])
def add_task():
    form = TaskForm()
    # populate category choices (id, name), include empty option
    categories = Category.query.order_by(Category.name).all()
    form.category.choices = [(0, "No category")] + [(c.id, c.name) for c in categories]
    if form.validate_on_submit():
        category_id = form.category.data or None
        if category_id == 0:
            category_id = None
        task = Task(
            title=form.title.data.strip(),
            description=form.description.data.strip() or None,
            deadline=form.deadline.data,
            completed=form.completed.data,
            category_id=category_id
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added.", "success")
        return redirect(url_for("index"))
    return render_template("add_task.html", form=form)




@app.route("/task/<int:task_id>/edit", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm()
    categories = Category.query.order_by(Category.name).all()
    form.category.choices = [(0, "No category")] + [(c.id, c.name) for c in categories]
    
    if request.method == "GET":
        form.title.data = task.title
        form.description.data = task.description
        form.deadline.data = task.deadline
        form.completed.data = task.completed
        form.category.data = task.category_id or 0

    if form.validate_on_submit():
        task.title = form.title.data.strip()
        task.description = form.description.data.strip() or None
        task.deadline = form.deadline.data
        task.completed = form.completed.data
        cid = form.category.data
        task.category_id = None if cid == 0 else cid
        db.session.commit()
        flash("Task updated.", "success")
        return redirect(url_for("index"))
    
    return render_template("edit_task.html", form=form, task=task)



@app.route("/task/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted.", "info")
    return redirect(url_for("index"))



@app.route("/task/<int:task_id>/toggle", methods=["POST"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    status = "completed" if task.completed else "incomplete"
    flash(f"Task marked {status}.", "success")
    return redirect(url_for("index"))
