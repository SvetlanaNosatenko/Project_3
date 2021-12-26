from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_page(self, page):
        limit = 12
        start = (page - 1) * limit
        return self.session.query(Director).limit(limit).offset(start).all()
