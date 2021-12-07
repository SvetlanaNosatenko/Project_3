from flask_restx import Resource, Namespace
from dao.model.director import DirectorSchema


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return DirectorSchema(many=True).dump(directors), 200