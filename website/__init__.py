from flask import Flask


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

    # Import blueprints
    from .views import views
    from .auth import auth

    # Register blueprints with URL prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
