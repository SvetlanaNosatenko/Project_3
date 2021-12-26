import base64
import hashlib
import hmac

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create(self, user_d):
        user_d["password"] = self.get_hash(user_d.get('password'))
        return self.dao.create(user_d)

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def update(self, user_d):
        user_d["password"] = self.get_hash(user_d.get('password'))
        return self.dao.update(user_d)

    def partially_update(self, user_d):
        user = self.get_one(user_d.get("id"))
        if "name" in user_d:
            user.name = user_d.get("name")
        if "surname" in user_d:
            user.surname = user_d.get("surname")
        if "password_1" and "password_2" in user_d:
            com = self.compare_passwords(password_hash=user.password, password=user_d.get('password_1'))
            if com:
                user.password = self.get_hash(user_d.get('password_2'))
        if "email" in user_d:
            user.email = user_d.get("email")
        if "favorite_genre" in user_d:
            user.favorite_genre = user_d.get("favorite_genre")
        return self.dao.update(user)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS))

    def compare_passwords(self, password_hash, password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )
