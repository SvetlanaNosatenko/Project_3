from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        return MovieSchema(many=True).dump(movies)


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        movie = movie_service.get_one(bid)
        return MovieSchema().dump(movie)

