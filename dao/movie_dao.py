from dao.model.movies_model import MovieModel


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get(self, params, mid=None):
        movie = self.session.query(MovieModel)
        if "director_id" in params:
            movie = movie.filter(MovieModel.director_id == params.get("director_id"))
            return movie
        if mid:
            movie = movie.get(mid)
            return movie
        return movie.all()

    def create(self, data):
        movie = MovieModel(**data)
        self.session.add(movie)
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get(mid)
        self.session.delete(movie)
        self.session.commit()