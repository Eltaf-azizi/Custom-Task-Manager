from datetime import datetime
from . import db



class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    tasks = db.relationship("Task", backref="category", lazy="dynamic", cascade="all, delete")


    def __repr__(self):
        return f"<Category {self.name}>"
