import jwt
from flask_restx import Resource, Namespace

from auth import auth_required, auth_check, jwt_decode
from constants import secret, algo
from dao.model.favorite import FavoriteSchema
from implemented import favorite_service, user_service

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies')
class FavoritesView(Resource):
    @auth_required
    def get(self):
        """ получить все фильмы пользователя из Избранного"""
        email = auth_check()["email"]
        print(email)
        user_id = user_service.get_id(email)
        all_favorite = favorite_service.get_by_user_id(user_id)
        res = FavoriteSchema(many=True).dump(all_favorite)
        return res, 200



@favorite_ns.route('/movies/<int:mid>')
class FavoriteView(Resource):
    @auth_required
    def delete(self, mid):
        """удалить фильм из Избранного"""
        email = auth_check()["email"]
        user_id = user_service.get_id(email)
        return favorite_service.delete(user_id=user_id, mid=mid), 201

    @auth_required
    def post(self, mid):
        """добавить фильм к пользователю в Избранное"""
        email = auth_check()["email"]
        print(email)
        user_id = user_service.get_id(email)
        data = {"user_id": user_id, "movie_id": mid}
        new_obj = favorite_service.create(data)
        return FavoriteSchema().dump(new_obj), 201







