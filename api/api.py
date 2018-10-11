from flask import abort
from flask_restful import Resource, reqparse


parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('query', required=True)


class SearchResource(Resource):
    def get(self):
        query = parser.parse_args()['query']
        if not query:
            abort(400, 'query must not be empty.')
