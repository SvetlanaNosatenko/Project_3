from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Kubrick')
    director_2 = Director(id=2, name='Spielberg')
    director_3 = Director(id=3, name='Tarkovsky')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    return director_dao


@pytest.fixture
def page():
    page = 3
    return page


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    @pytest.fixture
    def test_get_all(self, page):
        directors = self.director_service.get_all(page=page)
        assert len(directors) > 0
