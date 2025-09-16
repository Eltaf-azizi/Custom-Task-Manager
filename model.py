from datetime import datetime
from . import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    tasks = db.relationship("Task", backref="category", lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"

