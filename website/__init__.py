from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Initialize SQLAlchemy and set the database file name
db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    """
    Create a Flask application instance.

    Returns:
        Flask: The Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mimikamaishuuuuu'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    # Register blueprints for views and authentication
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        # Create the database tables based on the defined models
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """
        Load a user by their ID.

        Args:
            id: User ID.

        Returns:
            User: The User object corresponding to the ID.
        """
        return User.query.get(int(id))

    return app


def create_database(app):
    """
    Create the database if it does not exist.

    Args:
        app (Flask): The Flask application instance.
    """
    if not path.exists('website/' + DB_NAME):
        # Create the database tables
        db.create_all(app=app)
        print('Created Database!')