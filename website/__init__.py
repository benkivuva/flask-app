from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy database instance
db = SQLAlchemy()

# Define the database file name
DB_NAME = "database.db"

def create_app():
    """
    Create and configure a Flask application instance.

    Returns:
        Flask: The configured Flask application instance.
    """
    # Create the Flask app instance
    app = Flask(__name__)

    # Set the SECRET_KEY for session management
    app.config['SECRET_KEY'] = 'mimikamaishuuuuu'

    # Configure the SQLAlchemy database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Initialize the SQLAlchemy extension with the app
    db.init_app(app)

    # Import blueprints for modularization
    from .views import views
    from .auth import auth

    # Register blueprints with URL prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app