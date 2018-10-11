import os

from data.movie_store import MovieStore
from data.movie_doc_source import FakeDataSource, MovieDataSource
from data.util.imdb_scraper import FakeScraper, ImdbScraper
from flask import Flask
from flask_restful import Api
from api.api import MovieSearchResource


def create_app():
    # create and configure the app
    app = Flask(__name__)
    api = Api(app)
    # To play with mock data, feel free to swap out
    # - MovieDataSource <-> FakeDataSource or
    # - ImdbScraper <-> FakeScraper
    movie_store = MovieStore(MovieDataSource(ImdbScraper()))
    # Avoid running expensive init work twice. See https://stackoverflow.com/a/9476701
    if os.environ.get("WERKZEUG_RUN_MAIN"):
        movie_store.initialize()
    api.add_resource(MovieSearchResource,
                     '/search',
                     resource_class_kwargs={'movie_store': movie_store})

    return app
