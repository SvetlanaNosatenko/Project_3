from unittest.mock import MagicMock
import pytest
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1, title='Movie_1', description='description_1', trailer='trailer_1', year=2018,
                    rating=1, genre_id=1, director_id=2)
    movie_2 = Movie(id=2, title='Movie_2', description='description_2', trailer='trailer_2', year=2019,
                    rating=3, genre_id=2, director_id=7)
    movie_3 = Movie(id=3, title='Movie_3', description='description_3', trailer='trailer_3', year=2020,
                    rating=5, genre_id=5, director_id=9)
    movie_4 = Movie(id=4, title='Movie_4', description='description_4', trailer='trailer_4', year=2021,
                    rating=5, genre_id=5, director_id=9)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.get_genre = MagicMock(return_value=[movie_3, movie_4])
    movie_dao.get_director = MagicMock(return_value=[movie_3, movie_4])

    return movie_dao


@pytest.fixture
def dict_movie():
    dict_movie = {"page": 3,
                  "state": "new"}
    return dict_movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    @pytest.fixture
    def test_get_all(self, dict_movie):
        movies = self.movie_service.get_all(dict_movie=dict_movie)
        assert len(movies) > 0

    def test_get_genre(self):
        movies = self.movie_service.get_genre(5)
        assert len(movies) == 2

    def test_get_director(self):
        movies = self.movie_service.get_director(9)
        assert len(movies) == 2
