from dao.favorite import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def create(self, favorite_d):
        return self.dao.create(favorite_d)

    def delete(self, mid):
        self.dao.delete(mid)