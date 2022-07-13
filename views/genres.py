from flask_restx import Resource, Namespace
from dao.model.genres_model import GenreSchema
from implemented import genre_service


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    schemas = GenreSchema(many=True)

    def get(self):
        try:
            genres = self.schemas.dump(genre_service.get_g())
            return genres, 200
        except Exception as e:
            return e, 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    schemas = GenreSchema()

    def get(self, gid):
        try:
            genre = self.schemas.dump(genre_service.get_g(gid))
            return genre, 200
        except Exception as e:
            return e, 404