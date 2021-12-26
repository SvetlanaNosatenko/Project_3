from flask import request
from sqlalchemy import desc
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_director(self, bid):
        return self.session.query(Movie).filter(Movie.director_id == bid).all()

    def get_genre(self, bid):
        return self.session.query(Movie).filter(Movie.genre_id == bid).all()

    def get_all(self):
        """Для эндпонта  GET / movies / добавить необязательный параметр state.
        Если он присутствует и имеет значение new — возвращаем записи в отсортированном виде(самые свежие),
        иначе возвращаем в том порядке, в котором они лежат в базе."""

        return self.session.query(Movie).all()

    def get_page(self, page):
        limit = 6
        start = (page - 1) * limit
        return self.session.query(Movie).limit(limit).offset(start).all()

    def get_state(self):
        return self.session.query(Movie).order_by(desc(Movie.year)).all()

