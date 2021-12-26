from flask import request
from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        page = int(request.args.get("page", 1))
        directors = director_service.get_all(page)
        return DirectorSchema(many=True).dump(directors), 200
