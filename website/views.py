from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    """
    Render the home page.

    Returns:
        str: HTML content for the home page.
    """
    return render_template("home.html", user=current_user)
