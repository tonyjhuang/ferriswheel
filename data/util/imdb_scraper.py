import requests
from bs4 import BeautifulSoup

LIST_PAGE = "https://www.imdb.com/search/title?groups=top_1000&page={}&sort=user_rating"


class ImdbScraper:
    def __init__(self):
        self.list_pages = [LIST_PAGE.format(i) for i in range(1, 21)]

    @staticmethod
    def parse_content_div(div):
        people_tag = div.find_all('p')[2]
        return {
            'title': div.h3.a.text,
            'year': div.h3.find_all('span')[1].text[1:-1],
            'genres': div.find(class_='genre').text.strip().split(', '),
            # For the people, only use their last name
            'director': people_tag.a.text.split()[-1],
            'actors': map(lambda a: a.text.split()[-1], people_tag.find_all('a')[1:]),
        }

    def scrape(self):
        res = []
        print "scraping..."
        for i in range(len(self.list_pages)):
            list_page = self.list_pages[i]
            soup = BeautifulSoup(requests.get(list_page).text, 'html.parser')
            movies = map(ImdbScraper.parse_content_div,
                        soup.find_all(class_='lister-item-content'))
            res += movies
            print "finished {} out of {}".format(i+1, len(self.list_pages))
        return res


class FakeScraper:
    """Used for debugging"""

    def scrape(self):
        return [
            {
                'title': u't1',
                'year': u'2000',
                'genres': [u'horror', u'comedy'],
                'director': u'rick',
                'actors': [u'morty'],
            },
            {
                'title': u't2',
                'year': u'2012',
                'genres': [u'drama'],
                'director': u'beth',
                'actors': [u'jerry'],
            }
        ]
