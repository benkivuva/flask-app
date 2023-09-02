from flask import Blueprint, render_template

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


@views.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: HTML content for the home page.
    """
    return render_template("home.html")
