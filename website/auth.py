
"""
Authentication Blueprint

This module defines the authentication blueprint, which includes routes for
login, logout, and sign-up.

"""

from flask import Blueprint, render_template

# Create the 'auth' blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """
    Display the login page.
    """
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    """
    Log the user out.
    """
    return "<p>Log Out</p>"


@auth.route('/sign-up')
def sign_up():
    """
    Display the sign-up page.
    """
    return render_template("signup.html")
