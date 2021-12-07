from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return GenreSchema(many=True).dump(genres), 200
