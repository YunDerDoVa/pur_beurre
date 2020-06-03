import json
import requests


class OFFSearch:

    number_of_pages = None
    number_of_products = None
    dict = None

    def __init__(self, pages, products):

        self.number_of_pages = pages
        self.number_of_products = products

    def set_dict(self, dict):

        self.dict = dict


class OFFDatabase:

    searchs = []

    def get_connexion(self):
        """ This method return if the openfoodfacts' server is up. """

        url = (
            "https://world.openfoodfacts.org/cgi/search.pl"
        )
        payload = {
            'search_terms': 'Chocolat',
            'search_simple': 1,
            'action': 'process',
            'json': 1,
            'page_size': 10
        }
        r = requests.get(str(url), payload)
        page = json.loads(r.text)

        if True:
            return True
        else:
            return False

    def update_database(self):
        """ This method update the self.searchs after few minutes. """

        self.searchs = self._fetch_categories()

    def update_django(self):
        """ This method update django's database. """

        for search in self.searchs:
            for product in search:
                ## Add product in database
                pass


    def _get_categories(self, *argv):
        """ This private method retrun a list of String with the name of all
        categories we want to research. """

        if len(argv) > 0:
            categories = []
            for arg in argv:
                categories.append(arg)
        else:
            categories = [
                "fruits",
                "legumes",
                "frais",
                "sucres",
                "boissons",
                "viandes",
                "laits",
            ]

        return categories

    def _fetch_categories(self):
        """ This private method perform all searchs and
        return a list of Search. """
        pass

    def _search(self):
        """ This method make a search and return a json. """
        pass

    def _json_to_dict(self):
        """ This method convert a json to a dict more friendly with python and
        return the dict. """
        pass
