from whoosh.fields import Schema, KEYWORD, TEXT
from whoosh.filedb.filestore import RamStorage
from whoosh.qparser import QueryParser


SCHEMA = Schema(title=TEXT(stored=True), keywords=KEYWORD)


class MovieStore:
    def __init__(self, source):
        self.index = RamStorage().create_index(SCHEMA)
        writer = self.index.writer()
        for doc in source.get_docs():
            writer.add_document(**doc)
        writer.commit()

    def query(self, keywords):
        with self.index.searcher() as searcher:
            query = QueryParser("keywords", self.index.schema).parse(" ".join(keywords))
            return map(lambda res: str(res['title']), searcher.search(query))
