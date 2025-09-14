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
    