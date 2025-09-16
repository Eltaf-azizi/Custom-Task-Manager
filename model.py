from datetime import datetime
from . import db



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    tasks = db.relationship("Task", backref="category", lazy=True)


    def __repr__(self):
        return f"<Category {self.name}>"



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=True)


    def __repr__(self):
        return f"<Task {self.title}>"
