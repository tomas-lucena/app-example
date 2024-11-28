from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_model(app):
    db.init_app(app)
    with app.app_context():
        from .application import Application
                                
        db.create_all()