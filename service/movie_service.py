from dao.movie_dao import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, params):
        return self.dao.get(params)

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def create_m(self, data):
        return self.dao.create(data)

    def update_full(self, mid, data):
        movie = self.get_m(mid)
        movie.title = data["title"]
        movie.description = data["description"]
        movie.year = data["year"]
        movie.trailer = data["trailer"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]
        self.dao.update(movie)
        return movie

    def update_parts(self, mid, data):
        movie = self.get_m(mid)
        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "year" in data:
            movie.year = data["year"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "rating" in data:
            movie.rating = data["rating"]
        if "genre_id" in data:
            movie.genre_id = data["genre_id"]
        if "director_id" in data:
            movie.director_id = data["director_id"]
        self.dao.update(movie)
        return movie

    def delete_m(self, mid):
        self.dao.delete(mid)