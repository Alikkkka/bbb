from dao.genre_dao import GenreDAO


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_g(self, gid=None):
        return self.dao.get(gid)