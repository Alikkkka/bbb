from dao.director_dao import DirectorDAO


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_d(self, did=None):
        return self.dao.get(did)