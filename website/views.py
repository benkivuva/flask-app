from flask import Blueprint

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


@views.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: HTML content for the home page.
    """
    return "<h1>Test</h1>"
