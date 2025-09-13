from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Optional



class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=200)])
    description = TextAreaField("Description", validators=[Optional(), Length(max=2000)])
    deadline = DateField("Deadline (YYYY-MM-DD)", validators=[Optional()], format="%Y-%m-%d")
    category = SelectField("Category", coerce=int, validators=[Optional()])
    completed = BooleanField("Completed")
    submit = SubmitField("Save")



class CategoryForm(FlaskForm):
    name = StringField("Category name", validators=[DataRequired(), Length(max=120)])
    submit = SubmitField("Add")
