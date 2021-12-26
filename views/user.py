from flask import request
from flask_restx import Resource, Namespace
from dao.model.user import UserSchema
from implemented import user_service
from auth import auth_required

user_ns = Namespace('users')


@user_ns.route('/<int:bid>')
class UserView(Resource):
    @auth_required
    def get(self, bid):
        user = user_service.get_one(bid)
        return UserSchema().dump(user), 200

    @auth_required
    def patch(self, bid):
        """Изменить информацию пользователя (имя, фамилия, любимый жанр)"""
        req_json = request.json
        req_json["id"] = bid
        user_service.partially_update(req_json)
        return "", 204


@user_ns.route('/password/<int:uid>')
class UserView(Resource):
    """Обновить пароль пользователя, для этого нужно отправить два пароля password_1 и password_2."""
    @auth_required
    def put(self, uid):
        req_json = request.json
        req_json["id"] = uid
        user_service.partially_update(req_json)
        return "", 204

