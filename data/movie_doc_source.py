from util.imdb_scraper import ImdbScraper, FakeScraper
import json

FILENAME = "movies.db"


class MovieDataSource:
    """Fetches movie data from either disk or the web. Handles persistence via file i/o."""
    def __init__(self, scraper):
        self.scraper = scraper

    def movie_to_doc(self, movie):
        """Converts movie data to an indexable document"""
        keywords = []
        keywords.append(movie['year'])
        keywords += movie['genres']
        keywords.append(movie['director'])
        keywords += movie['actors']
        return {
            'title': movie['title'],
            'keywords': map(lambda keyword: keyword.lower(), keywords)
        }

    def __persist(self, documents):
        with open(FILENAME, "wb") as f:
            f.write(json.dumps(documents))

    def get_documents(self):
        try:
            with open(FILENAME, "r") as f:
                print "reading from persisted file"
                return json.load(f)
        except IOError:
            print "running scraper"
            movies = self.scraper.scrape()
            documents = map(self.movie_to_doc, movies)
            self.__persist(documents)
            return documents


class FakeDataSource:
    """Used for debugging"""
    def get_documents(self):
        return [
            {'title': u'Saving Private Ryan', 'keywords': [u'spielberg', u'hanks']},
            {'title': u'Find Mr Nemo', 'keywords': [u'fish', u'spielberg']},
        ]
