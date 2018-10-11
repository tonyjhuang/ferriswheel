from whoosh.fields import Schema, KEYWORD, TEXT
from whoosh.filedb.filestore import RamStorage
from whoosh.qparser import QueryParser


SCHEMA = Schema(title=TEXT(stored=True), keywords=KEYWORD)


class MovieStore:
    """Interface for searching movies by keyword."""
    def __init__(self, data_source):
        self.index = RamStorage().create_index(SCHEMA)
        self.data_source = data_source

    def initialize(self):
        writer = self.index.writer()
        for doc in self.data_source.get_documents():
            writer.add_document(**doc)
        writer.commit()

    def query_for_titles(self, keywords):
        with self.index.searcher() as searcher:
            query = QueryParser("keywords", self.index.schema).parse(" ".join(keywords))
            return map(lambda res: str(res['title']), searcher.search(query))
