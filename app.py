from flask import Flask
from flask_restx import Api
from config import Config
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns
from setup_db import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
     db.init_app(app)
     api = Api(app)
     api.add_namespace(movie_ns)
     api.add_namespace(genre_ns)
     api.add_namespace(director_ns)


application = create_app(Config())
debug = True


if __name__ == '__main__':
    application.run(port=1470, debug=True)
