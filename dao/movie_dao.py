from dao.model.movies_model import MovieModel


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get(self, params):
        movie = self.session.query(MovieModel)
        if "director_id" in params:
            movie = movie.filter(MovieModel.director_id == params.get("director_id"))
        if "genre_id" in params:
            movie = movie.filter(MovieModel.genre_id == params.get("genre_id"))
        if "year" in params:
            movie = movie.filter(MovieModel.year == params.get("year"))
        return movie.all()

    def get_one(self, mid):
        movie = self.session.query(MovieModel).get(mid)
        return movie

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