from dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, bid):
        return self.movie_dao.get_one(bid)

    def get_genre(self, bid):
        return self.movie_dao.get_genre(bid)

    def get_director(self, bid):
        return self.movie_dao.get_director(bid)

    def get_all(self, dict_movie):

        if dict_movie.get("state") is not None and dict_movie.get("state") == "new":
            result = self.movie_dao.get_state()

        elif dict_movie.get("page") is not None:
            result = self.movie_dao.get_page(dict_movie.get("page"))

        else:
            result = self.movie_dao.get_all()

        return result
