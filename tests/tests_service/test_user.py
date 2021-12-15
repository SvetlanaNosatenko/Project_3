from unittest.mock import MagicMock
import pytest
from dao.user import UserDAO
from dao.model.user import User
from service.user import UserService


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    user_1 = User(id=1, name='Name_1', surname='Surname_1', password='password_1', email='email_1',
                  favorite_genre='favorite_genre')

    user_dao.get_one = MagicMock(return_value=user_1)
    user_dao.create = MagicMock(return_value=User(id=1))
    user_dao.update = MagicMock()
    return user_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.user_service.get_one(1)
        assert user is not None
        assert user.id is not None

    def test_create(self):
        user_d = {
            'name': 'Name_1',
            'surname': 'Surname_1',
            'password': 'password_1',
            'email': 'email_1',
            'favorite_genre': 'favorite_genre'
        }
        user = self.user_service.create(user_d)
        assert user.id is not None

    def test_update(self):
        user_d = {'id': 1,
                  'name': 'Name_2',
                  'surname': 'Surname_1',
                  'password': 'password_2',
                  'email': 'email_1',
                  'favorite_genre': 'favorite_genre'
                  }
        self.user_service.update(user_d)

    def test_partially_update(self):
        user_d = {'id': 2,
                  'name': 'Name_3',
                  'surname': 'Surname_1',
                  'password': 'password_2',
                  'email': 'email_1',
                  'favorite_genre': 'favorite_genre'
                  }
        self.user_service.partially_update(user_d)
