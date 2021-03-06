from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genres_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name='Horror')
    genre_2 = Genre(id=2, name='Comedy')
    genre_3 = Genre(id=3, name='Thriller')

    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])

    return genre_dao


@pytest.fixture()
def page():
    return 3


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genres_dao):
        self.genre_service = GenreService(genre_dao=genres_dao)

    @pytest.fixture
    def test_get_all(self, page):
        genres = self.genre_service.get_all(page=page)
        assert len(genres) > 0
