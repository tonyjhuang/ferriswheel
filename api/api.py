from flask import abort
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('query', required=True)


class MovieSearchResource(Resource):
    def __init__(self, **kwargs):
        self.store = kwargs['movie_store']

    def get(self):
        query = parser.parse_args()['query']
        keywords = map(lambda k: k.lower(), query.split(","))
        if not keywords:
            abort(400, 'query must not be empty.')
        return {'res': self.store.query(keywords)}
