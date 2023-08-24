
"""
Authentication Blueprint

This module defines the authentication blueprint, which includes routes for
login, logout, and sign-up.

"""

from flask import Blueprint

# Create the 'auth' blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """
    Display the login page.
    """
    return "<p>Login</p>"


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
    return "<p>Sign Up</p>"
