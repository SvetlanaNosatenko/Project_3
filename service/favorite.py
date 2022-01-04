from dao.favorite import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_by_user_id(self, user_id):
        return self.dao.get_by_user_id(user_id)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, user_id, mid):
        self.dao.delete(user_id, mid)



