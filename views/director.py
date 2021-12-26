from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from dao.model.movie import MovieSchema
from implemented import director_service, movie_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page = int(request.args.get("page", 1))
        directors = director_service.get_all(page)
        return DirectorSchema(many=True).dump(directors), 200


# @director_ns.route('/<int:bid>')
# class DirectorView(Resource):
#     def get(self, bid):
#         director = movie_service.get_director(bid)
#         return MovieSchema().dump(director), 200