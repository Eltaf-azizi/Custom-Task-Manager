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


## ⚙️ Setup & Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/custom-task-manager.git
cd custom-task-manager
```

2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

3. Run the app:
```
python run.py
```

4. Open in browser:
```
http://127.0.0.1:5000/
```


🎯 Why I Built This

I wanted to build something practical while practicing the fundamentals:

 - How to design a project structure
 - How Flask works with SQLite
 - How to perform CRUD operations
 - How to make a simple front end look clean with CSS

This project might look simple, but for me it was a big step toward learning how real applications are built.

