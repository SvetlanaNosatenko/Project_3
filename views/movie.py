from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        page = int(request.args.get("page", 1))
        state = request.args.get('state')
        dict_movie = {"page": page,
                      "state": state}
        movies = movie_service.get_all(dict_movie)
        return MovieSchema(many=True).dump(movies)


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        movie = movie_service.get_one(bid)
        return MovieSchema().dump(movie)


@movie_ns.route('/genres/<int:bid>')
class MovesGenreView(Resource):
    def get(self, bid):
        movie = movie_service.get_genre(bid)
        return MovieSchema().dump(movie)


@movie_ns.route('/directors/<int:bid>')
class MovesDirectorView(Resource):
    def get(self, bid):
        movie = movie_service.get_director(bid)
        return MovieSchema().dump(movie)

