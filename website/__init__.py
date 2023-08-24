from flask import Flask


def create_app():
    """
    Create and configure a Flask application instance.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mimikamaishuuuuu'

    return app
