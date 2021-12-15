from flask import request

from dao.model.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        user = request.args.get('user')
        return self.session.query(Favorite).filter(Favorite.user_id == user).all()

    def create(self, favorite_d):
        ent = Favorite(**favorite_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, mid):
        favorite = self.session.query(Favorite).filter(Favorite.movie_id == mid).all()
        self.session.delete(favorite)
        self.session.commit()

