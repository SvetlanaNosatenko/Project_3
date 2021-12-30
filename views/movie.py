from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    """Для тех эндпоинтов, которые возвращают несколько записей, организовать пагинацию через URL-параметр page
    (возвращать на страницу по 12 элементов).
    Для эндпонта GET /movies/ добавить необязательный параметр state.
    Если он присутствует и имеет значение new — возвращаем записи в отсортированном виде (самые свежие),
    иначе возвращаем в том порядке, в котором они лежат в базе."""
    def get(self):
        page = int(request.args.get("page", 1))
        state = request.args.get('state')
        dict_movie = {"page": page,
                      "state": state}
        movies = movie_service.get_all(dict_movie)
        return MovieSchema(many=True).dump(movies)


@movie_ns.route('/<int:bid>')
class MovieView(Resource):
    def get(self, bid):
        movie = movie_service.get_one(bid)
        return MovieSchema().dump(movie)


@movie_ns.route('/genres/<int:bid>')
class MovesGenreView(Resource):
    """Получение списка фильмом по определенному жанру"""
    def get(self, bid):
        movie = movie_service.get_genre(bid)
        return MovieSchema(many=True).dump(movie)


@movie_ns.route('/directors/<int:bid>')
class MovesDirectorView(Resource):
    """Получение списка фильмом по определенному режиссеру"""
    def get(self, bid):
        movie = movie_service.get_director(bid)
        return MovieSchema(many=True).dump(movie)

