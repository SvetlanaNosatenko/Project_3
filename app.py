from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db
from views.director import director_ns
from views.favorite import favorite_ns
from views.genre import genre_ns
from views.movie import movie_ns
from views.user import user_ns
from data import data


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(user_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(favorite_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()

        for movie in data["movies"]:
            m = Movie(
                id=movie["pk"],
                title=movie["title"],
                description=movie["description"],
                trailer=movie["trailer"],
                year=movie["year"],
                rating=movie["rating"],
                genre_id=movie["genre_id"],
                director_id=movie["director_id"],
            )
            with db.session.begin():
                db.session.add(m)

        for director in data["directors"]:
            d = Director(
                id=director["pk"],
                name=director["name"],
            )
            with db.session.begin():
                db.session.add(d)

        for genre in data["genres"]:
            g = Genre(
                id=genre["pk"],
                name=genre["name"],
            )

            with db.session.begin():
                db.session.add(g)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)