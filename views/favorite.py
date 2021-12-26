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


@favorite_ns.route('/movies/<int:mid>')
class FavoriteView(Resource):
    @auth_required
    def delete(self, mid):
        req_json = request.json
        req_json["movie_id"] = mid
        favorite_service.delete(mid)
        return "", 204


    @auth_required
    def post(self, mid):
        req_json = request.json
        req_json["movie_id"] = mid
        favorite_service.create(req_json)
        return "", 201


