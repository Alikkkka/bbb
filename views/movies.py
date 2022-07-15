from flask_restx import Resource, Namespace
from dao.model.movies_model import MovieSchema
from implemented import movie_service
from flask import request, make_response, jsonify

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    schemas = MovieSchema(many=True)

    def get(self):
        movies = self.schemas.dump(movie_service.get_all(request.args))
        return movies, 200

    def post(self):
        try:
            movie = movie_service.create_m(request.json)
            resp = make_response("", 201)
            resp.headers['location'] = f'{movie_ns.path}/{movie.id}'
            return resp
        except Exception as e:
            return e, 404


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    schema = MovieSchema()

    def get(self, mid):
        try:
            movie = self.schema.dump(movie_service.get_one(mid))
            return movie, 200
        except Exception as e:
            return e, 404

    def put(self, mid):
        try:
            movie = self.schema.dump(movie_service.update_full(mid, request.json))
            return movie, 200
        except Exception as e:
            return e, 404

    def patch(self, mid):
        try:
            movie = self.schema.dump(movie_service.update_parts(mid, request.json))
            return movie, 200
        except Exception as e:
            return e, 404

    def delete(self, mid):
        try:
            movie_service.delete_m(mid)
        except Exception as e:
            return e, 404