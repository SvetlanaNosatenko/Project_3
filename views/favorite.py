from flask import request
from flask_restx import Resource, Namespace

from auth import auth_required
from dao.model.favorite import FavoriteSchema
from implemented import favorite_service

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies')
class FavoritesView(Resource):
    @auth_required
    def get(self):
        all_favorite = favorite_service.get_all()
        res = FavoriteSchema(many=True).dump(all_favorite)
        return res, 200

    def post(self):
        req_json = request.json
        favorite_service.create(req_json)
        return "", 201


@favorite_ns.route('/movies/<int:movie_id>')
class FavoriteView(Resource):
    def delete(self, mid):
        favorite_service.delete(mid)
        return "", 204

