from dao.favorite import FavoriteDAO
from dao.movie import MovieDAO
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.user import UserDAO
from service.favorite import FavoriteService
from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService
from service.user import UserService
from setup_db import db

movie_dao = MovieDAO(session=db.session)
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
user_dao = UserDAO(session=db.session)
favorite_dao = FavoriteDAO(session=db.session)

movie_service = MovieService(dao=movie_dao)
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
user_service = UserService(dao=user_dao)
favorite_service = FavoriteService(dao=favorite_dao)