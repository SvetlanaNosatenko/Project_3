from dao.genre import GenreDAO
from dao.movie import MovieDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self, page):
        if page is not None:
            result = self.genre_dao.get_page(page)
        else:
            result = self.genre_dao.get_all()
        return result
