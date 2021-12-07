from flask_restx import Resource, Namespace

from dao.model.favorite import FavoriteSchema

favorite_ns = Namespace('favorites')


@favorite_ns.route('/')
class FavoriteView(Resource):
    def get(self):
        all_users = favorite_service.get_all()
        res = FavoriteSchema(many=True).dump(all_users)
        return res, 200