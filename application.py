import os


from flask import Flask


from extensions import db
from views import blueprint
import commands


def create_app():
    app = Flask(__name__.split('.')[0])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
        os.environ.get('SQLALCHEMY_DATABASE_URI', 'realty.db'))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(blueprint)
    register_commands(app)
    return app


def register_commands(app):
    app.cli.add_command(commands.create)
    app.cli.add_command(commands.drop)
    app.cli.add_command(commands.feed)
