from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self, page):
        if page is not None:
            result = self.dao.get_page(page)
        else:
            result = self.dao.get_all()
        return result

