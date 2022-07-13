from flask_restx import Resource, Namespace, Api
from dao.model.directors_model import DirectorSchema, DirectorModel
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    schemas = DirectorSchema(many=True)

    def get(self):
        try:
            directors = self.schemas.dump(director_service.get_d())
            return directors, 200
        except Exception as e:
            return e, 404


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    schema = DirectorSchema()

    def get(self, did):
        try:
            director = self.schema.dump(director_service.get_d(did))
            return director, 200
        except Exception as e:
            return e, 404