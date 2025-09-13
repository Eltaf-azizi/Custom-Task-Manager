import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()



def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)


    # ensure instance folder exists
    try:
        os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'instance'), exist_ok=True)
    except OSError:
        pass


    db.init_app(app)


    with app.app_context():
        # import routes so they are registered
        from . import routes, models
        # create DB if it doesn't exist
        db.create_all()


    return app

