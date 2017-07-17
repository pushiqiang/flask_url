"""
WSGI config for canting project.

It exposes the WSGI callable as a module-level variable named ``application``.

"""

from blog import app

if __name__ == "__main__":
    app.run()
