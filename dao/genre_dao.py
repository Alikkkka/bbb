from dao.model.genres_model import GenreModel


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get(self, gid=None):
        genre = self.session.query(GenreModel)
        if gid:
            genre = genre.get(gid)
            return genre
        return genre.all()