from flask import request
from flask_restx import Resource, Namespace

from dao.model.schema import MovieSchema
from implement import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MovieViews(Resource):
    def get(self):
        args = request.args
        if len(args):
            return movie_schema.dump(movie_service.get_movie_by_kwargs(**args)), 200

        return movie_schema.dump(movie_service.get_movies()), 200
    #
    def post(self):
        if movie_service.create_movie(**request.json):
            return 'создано', 200
        else:
            return 'ошибка', 200


@movie_ns.route('/<int:uid>')
class MovieViews(Resource):
    def get(self, uid):
        return movie_schema.dump([movie_service.get_movie_by_id(uid=uid)]), 200

    def put(self, uid):
        if movie_service.update_movie(uid, **request.json):
            return 'обновился', 200
        else:
            return 'необновился', 200

    def delete(self, uid):
        if movie_service.delete_movie(uid):
            return 'удален', 200
        else:
            return 'неудален', 200
