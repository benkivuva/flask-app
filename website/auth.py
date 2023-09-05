
"""
Authentication Blueprint

This module defines the authentication blueprint, which includes routes for
login, logout, and sign-up.

"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

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
            flash('Email is too short', category='error')
        elif len(first_name) < 2:
            flash('Name must be grater than two characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password  is too short', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html")
