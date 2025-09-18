<h1 align="center">Custom-Task-Manager</h1>


This is my first full CRUD web application built with Flask and SQLite.
I created it as part of my learning journey to understand how to structure real projects, connect a database, and build something practical that I can use.

The goal of this project was simple:

👉 Learn how to create, read, update, and delete (CRUD) data in a real app.


## 🚀 Features

 - Add new tasks with deadlines
 - Organize tasks by categories
 - Edit and update tasks anytime
 - Mark tasks as completed
 - Delete tasks or categories
 - Simple, clean UI with custom CSS


## Project Structure

    custom-task-manager/
    ├── README.md                 # Project documentation
    ├── requirements.txt          # Dependencies
    ├── .gitignore                # Ignore venv, db files, cache
    ├── config.py                 # App configuration
    ├── run.py                    # Entry point
    ├── instance/                 # SQLite DB stored here
    │   └── taskmanager.db
    └── app/
        ├── __init__.py           # App factory + DB init
        ├── models.py             # Task + Category models
        ├── routes.py             # CRUD routes
        ├── templates/            # HTML templates
        │   ├── base.html
        │   ├── index.html
        │   ├── add_task.html
        │   ├── edit_task.html
        │   └── categories.html
        └── static/               # CSS + JS
            ├── style.css
            └── script.js
