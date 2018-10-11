from flask import Flask, abort
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('query', required=True)


class SearchResource(Resource):
    def get(self):
        query = parser.parse_args()['query']
        if not query:
            abort(400, 'query must not be empty.')
        return ""


api.add_resource(SearchResource, '/search')


@app.errorhandler(404)
def not_found(e):
    return '', 404
