import calendar
import datetime
import hashlib

from flask_restx import Resource, Namespace
from flask import abort, request
import jwt
from constants import *
from dao.model.user import User
from implemented import user_service
from setup_db import db

auth_ns = Namespace('auth')


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, secret, algorithms=algo)
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


@auth_ns.route('/register')
class UsersView(Resource):
    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        email = req_json.get('email')
        password = req_json.get('password')

        if None in [email, password]:
            abort(400)

        user = db.session.query(User).filter(User.email == email).first()

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        compare = user_service.compare_passwords(password_hash=user.password, password=password)

        if not compare:
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "email": user.email
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)

        return {"access_token": access_token, "refresh_token": refresh_token}, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(400)

        data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])

        email = data.get("email")
        user = db.session.query(User).filter(User.email == email).first()

        data = {"email": user.email}
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)

        return {"access_token": access_token, "refresh_token": refresh_token}, 201