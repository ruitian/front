# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_script import Shell
from flask_script import Server

from app import app


manager = Manager(app)


def make_shell_context():
    return dict(
        app=app)

manager.add_command("runserver", Server(host="0.0.0.0", port="5000"))
manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
