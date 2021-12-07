from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all()
        return MovieSchema(many=True).dump(movies), 200