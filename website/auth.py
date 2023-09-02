
"""
Authentication Blueprint

This module defines the authentication blueprint, which includes routes for
login, logout, and sign-up.

"""

from flask import Blueprint, render_template, request

# Create the 'auth' blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
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


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Display the sign-up page.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif password1 < 7:
            pass
        else:
            # add user to db
            pass
    return render_template("signup.html")
