from dao.favorite import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def create(self, favorite_d):
        return self.dao.create(favorite_d)

    def delete(self, favorite_id):
        self.dao.delete(favorite_id)

    def get_all_by_filter(self, favorite_id):
        return self.dao.get_all_by_filter(favorite_id)


