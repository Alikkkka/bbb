from marshmallow import Schema, fields

from setup_db import db


class GenreModel(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()