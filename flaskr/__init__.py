from data.movie_store import MovieStore
from data.movie_doc_source import FakeDataSource
from flask import Flask
from flask_restful import Api
from api.api import MovieSearchResource


def create_app():
    # create and configure the app
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(MovieSearchResource,
                     '/search',
                     resource_class_kwargs={'movie_store': MovieStore(FakeDataSource())})

    return app
