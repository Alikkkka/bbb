from dao.model.directors_model import DirectorModel


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get(self, did=None):
        dir = self.session.query(DirectorModel)
        if did:
            dir = dir.get(did)
            return dir
        return dir.all()