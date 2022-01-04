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
        self.session.add(user_d)
        self.session.commit()

    def get_id(self, email):
        user = self.session.query(User).filter(User.email == email).first()
        return user.id
