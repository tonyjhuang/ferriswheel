

class MovieDataSource:
    def __init__(self):
        pass

    def get_docs(self):
        return []


class FakeDataSource:
    def get_docs(self):
        return [
            {'title': u'Saving Private Ryan', 'keywords': [u'Spielberg', u'Hanks']},
            {'title': u'Find Mr Nemo', 'keywords': [u'Fish', u'Spielberg']},
        ]

