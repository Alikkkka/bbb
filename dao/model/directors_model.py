from setup_db import db
from marshmallow import Schema, fields


class DirectorModel(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    def __str__(self):
        return self.name


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()