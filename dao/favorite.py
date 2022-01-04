from flask import request

from dao.model.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_by_user_id(self, user_id):
        return self.session.query(Favorite).filter(Favorite.user_id == user_id).all()

    def create(self, data):
        ent = Favorite(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, user_id, mid):
        favorite_id = self.session.query(Favorite).filter(Favorite.movie_id == mid, Favorite.user_id == user_id).first()
        self.session.delete(favorite_id)
        self.session.commit()



