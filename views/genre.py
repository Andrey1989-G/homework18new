from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implement import director_service, genre_service

genre_ns = Namespace('directors')
genre_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenreViews(Resource):
    def get(self):
        return genre_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:uid>')
class GenreViews(Resource):
    def get(self, uid):
        return genre_schema.dump([director_service.get_genre_by_id(uid=uid)]), 200

