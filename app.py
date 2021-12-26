from flask import Flask, render_template
from flask_restx import Api
from auth import auth_ns
from config import Config
from setup_db import db
from views.director import director_ns
from views.favorite import favorite_ns
from views.genre import genre_ns
from views.movie import movie_ns
from views.user import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app=app)
    api = Api(title="Flask Course Project 3", doc="/docs")
    api.init_app(app)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(favorite_ns)
    api.add_namespace(auth_ns)

    return app


app = create_app(Config())
# register_extensions(app=app)

app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
