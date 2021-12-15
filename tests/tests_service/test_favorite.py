from unittest.mock import MagicMock
import pytest
from dao.favorite import FavoriteDAO
from dao.model.favorite import Favorite
from service.favorite import FavoriteService


@pytest.fixture()
def favorite_dao():
    favorite_dao = FavoriteDAO(None)

    favorite_1 = Favorite(id=1, user_id='User_1', movie_id='Movie_1')
    favorite_2 = Favorite(id=2, user_id='User_2', movie_id='Movie_2')
    favorite_3 = Favorite(id=3, user_id='User_3', movie_id='Movie_3')

    favorite_dao.get_all = MagicMock(return_value=[favorite_1, favorite_2, favorite_3])
    favorite_dao.create = MagicMock(return_value=Favorite(id=1))
    favorite_dao.delete = MagicMock()
    return favorite_dao


class TestFavoriteService:
    @pytest.fixture(autouse=True)
    def favorite_service(self, favorite_dao):
        self.favorite_service = FavoriteService(dao=favorite_dao)

    def test_get_all(self):
        favorites = self.favorite_service.get_all()
        assert len(favorites) > 0

    def test_create(self):
        favorite_d = {
            'user_id': 'user_id',
            'movie_id': 'movie_id'
        }
        favorite = self.favorite_service.create(favorite_d)
        assert favorite.id is not None

    def test_delete(self):
        self.favorite_service.delete(1)
