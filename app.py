from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from create_data import *
from models_schemas import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 3}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
movie_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        try:
            movie_with_filters = db.session.query(Movie.id, Movie.title, Movie.description,
                                              Movie.trailer)
            director_id = request.args.get('director_id')
            genre_id = request.args.get('genre_id')
            if director_id:
                movie_with_filters = movie_with_filters.filter(Movie.director_id == director_id)
            if genre_id:
                movie_with_filters = movie_with_filters.filter(Movie.genre_id == genre_id)

            movies_list = movie_with_filters.all()
            return movies_schema.dump(movies_list)
        except Exception as e:
            return 'Возникла ошибка !', 404


    def post(self):
        try:
            req_json = request.json
            posted_movie = Movie(**req_json)
            with db.session.begin():
                db.session.add(posted_movie)
            return "Фильм добавлен в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404


@movie_ns.route('/<int:movie_id>')
class MoviesView(Resource):
    def get(self, movie_id: int):
        try:
            movie_by_id = db.session.query(Movie.id, Movie.title, Movie.description,
                                              Movie.trailer).filter(Movie.id == movie_id).one()
            return movie_schema.dump(movie_by_id)
        except Exception as e:
            return 'Возникла ошибка !', 404


    def put(self, movie_id: int):
        try:
            req_json = request.json
            movie = db.session.query(Movie).get(movie_id)
            movie.title = req_json["title"]
            movie.description = req_json["description"]
            movie.trailer = req_json["trailer"]
            movie.year = req_json["year"]
            movie.rating = req_json["rating"]
            movie.genre_id = req_json["genre_id"]
            movie.director_id = req_json["director_id"]
            db.session.add(movie)
            return "Данные о фильме обновлены в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404

    def delete(self, movie_id: int):
        try:
            movie = db.session.query(Movie).get(movie_id)
            db.session.delete(movie)
            db.session.commit()
            return "Фильм удален из БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        try:
            directors = db.session.query(Director).all()
            return directors_schema.dump(directors)
        except Exception as e:
            return 'Возникла ошибка !', 404

    def post(self):
        try:
            req_json = request.json
            posted_dir = Director(**req_json)
            with db.session.begin():
                db.session.add(posted_dir)
            return "Режиссер добавлен в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404


@directors_ns.route('/<int:dir_id>')
class DirectorsView(Resource):
    def get(self, dir_id: int):
        try:
            director = db.session.query(Director).filter(Director.id == dir_id).one()
            return director_schema.dump(director)
        except Exception as e:
            return 'Возникла ошибка !', 404

    def put(self, dir_id: int):
        try:
            req_json = request.json
            dir = db.session.query(Director).get(dir_id)
            dir.name = req_json["name"]
            db.session.add(dir)
            return "Данные о режиссере обновлены в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404

    def delete(self, dir_id: int):
        try:
            dir = db.session.query(Director).get(dir_id)
            db.session.delete(dir)
            db.session.commit()
            return "Режиссер удален из БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            genres = db.session.query(Genre).all()
            return genres_schema.dump(genres)
        except Exception as e:
            return 'Возникла ошибка !', 404


    def post(self):
        try:
            req_json = request.json
            posted_genre = Genre(**req_json)
            with db.session.begin():
                db.session.add(posted_genre)
            return "Жанр добавлен в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404


@genres_ns.route('/<int:gen_id>')
class GenresView(Resource):
    def get(self, gen_id: int):
        try:
            genre = db.session.query(Genre).filter(Genre.id == gen_id).one()
            return genre_schema.dump(genre)
        except Exception as e:
            return 'Возникла ошибка !', 404

    def put(self, gen_id: int):
        try:
            req_json = request.json
            genre = db.session.query(Genre).get(gen_id)
            genre.name = req_json["name"]
            db.session.add(genre)
            return "Данные о жанре обновлены в БД!"
        except Exception as e:
            return 'Возникла ошибка !', 404

    def delete(self, gen_id: int):
            try:
                gen = db.session.query(Genre).filter(Genre.id == gen_id).one()
                db.session.delete(gen)
                db.session.commit()
                return "Жанр удален из БД!"
            except Exception as e:
                return 'Возникла ошибка !', 404


if __name__ == '__main__':
    app.run(debug=True, port=8881)
