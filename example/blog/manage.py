#-*-coding:utf-8-*-

from blog import app, settings
from flask_script import Manager, Shell


manager = Manager(app, with_default_commands=False)


def _make_context():
    return dict(app=app, settings=settings)


manager.add_command('shell', Shell(make_context=_make_context))


@manager.command
def runserver():
    app.run()


if __name__ == '__main__':
    manager.run()
