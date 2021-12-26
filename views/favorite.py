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
        """ получить все фильмы пользователя из Избранного"""
        all_favorite = favorite_service.get_all()
        res = FavoriteSchema(many=True).dump(all_favorite)
        return res, 200


@favorite_ns.route('/movies/<int:mid>')
class FavoriteView(Resource):
    @auth_required
    def delete(self, mid):
        """удалить фильм из Избранного"""
        favorite_id = favorite_service.get_all_by_filter({"user_id": user.get("id"), "movie_id": mid})[0].get("id")
        favorite_service.delete(favorite_id)
        return "", 201

    @auth_required
    def post(self, mid):
        """добавить фильм к пользователю в Избранное"""
        new_obj = favorite_service.create(
            {"user_id": user.get("id"), "movie_id": mid}
        )
        return new_obj, 201


