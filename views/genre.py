from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from dao.model.movie import MovieSchema
from implemented import genre_service, movie_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        page = int(request.args.get("page", 1))
        genres = genre_service.get_all(page)
        return GenreSchema(many=True).dump(genres), 200


@genre_ns.route('/<int:bid>')
class GenreView(Resource):
    def get(self, bid):
        genre = movie_service.get_genre(bid)
        return MovieSchema().dump(genre), 200

