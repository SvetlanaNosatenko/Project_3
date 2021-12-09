from flask import request

from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_all(self):
        page = int(request.args.get("page", 1))  # возвращает список всех фильмов, разделенный по страницам
        limit = 2
        start = (page - 1) * limit
        result = self.session.query(Genre).limit(limit).offset(start).all()
        return result