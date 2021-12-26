from dao.model.genre import Genre
from dao.model.movie import Movie


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_page(self, page):
        limit = 12
        start = (page - 1) * limit
        return self.session.query(Genre).limit(limit).offset(start).all()



