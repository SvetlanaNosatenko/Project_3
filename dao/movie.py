from flask import request
from sqlalchemy import desc

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)


    def get_all(self):
        """Для эндпонта  GET / movies / добавить необязательный параметр state.
        Если он присутствует и имеет значение new — возвращаем записи в отсортированном виде(самые свежие),
        иначе возвращаем в том порядке, в котором они лежат в базе."""

        state = request.args.get('state')
        page = int(request.args.get("page", 1))  # возвращает список всех фильмов, разделенный по страницам
        limit = 2
        start = (page - 1) * limit
        if state == "new":
            result = self.session.query(Movie).order_by(desc(Movie.year)).limit(limit).offset(start).all()
        else:
            result = self.session.query(Movie).limit(limit).offset(start).all()
        return result
