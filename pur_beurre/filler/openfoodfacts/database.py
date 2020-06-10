import json
import requests


from foodfinder.models import Food


class OFFSearch:

    category_index = None
    category = None
    number_of_pages = None
    number_of_products = None
    dict = None

    def __init__(self, category_index, category, pages, products):

        self.category_index = category_index
        self.category = category
        self.number_of_pages = pages
        self.number_of_products = products

    def set_dict(self, dict):

        self.dict = dict

        return self


class OFFDatabase:

    searchs = []

    def get_connexion(self):
        """ This method return if the openfoodfacts' server is up. """

        page = self._request()

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
            for product in search.dict.items():
                ## Add product in database
                Food.objects.create(
                    name=product['name']
                )

    def drop_django(self):
        """ This method drop django database """

        Food.objects.drop()

    def _request(self, **kwargs):
        """ This method make a search and return a json. """

        page_size = kwargs.pop('page_size', 10)
        page_index = kwargs.pop('page_index', None)
        search = kwargs.pop('search', 'Chocolat')

        url = kwargs.pop('url', "https://world.openfoodfacts.org/cgi/search.pl")
        payload = kwargs.pop('payload', {
            'search_terms': search,
            'search_simple': 1,
            'action': 'process',
            'json': 1,
            'page_size': page_size,
        })

        if page_index is not None:
            payload['page'] = page_index

        r = requests.get(str(url), payload)
        page = json.loads(r.text)

        return page

    def _get_categories(self, *argv):
        """ This private method retrun a list of String with the name of all
        categories we want to research. """

        if len(argv) > 0:
            categories = argv[0]
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

        categories = self._get_categories()

        page_size = 100

        for category in categories:
            beefeye = self.request(search=category)

            number_of_pages = int(int(beefeye["count"]) / page_size)
            number_of_products = int(beefeye["count"])

            for i in range(number_of_pages):
                print('Page ' + i+1 + '/' + number_of_pages + ' [search_terms=' + category + ']')
                page = self._request(page_size=page_size, page_index=i, search=category)

                for j in range(len(page['products'])):
                    product = page['products'][j]
                    category_index = i*page_size + j
                    dict = self._product_to_food_dict(product)

                    searchOFF = SearchOFF(category_index, category, number_of_pages, number_of_products)
                    self.searchs.append(searchOFF.set_dict(dict))

        return self.searchs


    def _search(self):
        """ This method make a search and return a json. """
        pass

    def _product_to_food_dict(self, product):
        """ This method convert a json to a dict more friendly with python and
        return the dict. """

        dict = {}

        dict['name'] = product['name']


        return dict
