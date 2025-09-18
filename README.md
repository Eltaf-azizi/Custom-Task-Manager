<h1 align="center">Custom-Task-Manager</h1>


A lightweight web-based task management system built with Flask and SQLite. This project is designed to help me (and anyone who uses it) learn and practice full-stack development concepts while creating something useful.

## 🚀 Features

 - Add, edit, and delete tasks
 - Organize tasks into categories
 - Mark tasks as complete or incomplete
 - View tasks in a clean, simple interface
 - Persistent storage using SQLite
 - Responsive design with custom CSS


🛠️ Tech Stack

 - Backend: Flask (Python)
 - Database: SQLite with SQLAlchemy ORM
 - Frontend: HTML, Jinja2 templates, CSS, JavaScript
 - Form Handling: Flask-WTF (for validation)

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


## 📜 License

This project is open source under the MIT License. Feel free to use it, learn from it, or even improve it.



**⚡ Written by me, Altaf Hussain** — as part of my learning journey in Python, Flask, and web development.
