from db_setup import db

from marshmallow import fields, Schema

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class MovieSchema(Schema):
    id = fields.Int()
    description = fields.Str()
    rating = fields.Float()
    title = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    director = fields.Nested(DirectorSchema)
    genre = fields.Nested(GenreSchema)
