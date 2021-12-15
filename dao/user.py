from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def update(self, user_d):
        user = self.get_one(user_d.get('id'))
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        user.password = user_d.get("password")
        user.email = user_d.get("email")
        user.favorite_genre = user_d.get("favorite_genre")
        self.session.add(user)
        self.session.commit()



