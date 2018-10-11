from flask import Flask
from flask_restful import Api
from api.api import SearchResource


def create_app():
    # create and configure the app
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(SearchResource, '/search')

    return app
