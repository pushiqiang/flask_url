#-*-coding:utf-8-*-

import sys

from blog import app, db, settings
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate


manager = Manager(app, with_default_commands=False)
migrate = Migrate(app, db)

def _make_context():
    return dict(app=app, db=db, settings=settings)

manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run()


@manager.command
def initdb():
    # TODO 优化引入
    from post.models import *
    try:
        db.create_all()
        print 'Create tables success:', e
    except Exception as e:
        print 'Create tables fail:', e
        sys.exit(0)


if __name__ == '__main__':
    manager.run()
