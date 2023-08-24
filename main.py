#!/usr/bin/env python
"""
Main Application Entry Point

This script starts the Flask application.

"""

from website import create_app

app = create_app()

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
