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

    def _product_to_food_dict(self, product):
        """ This method convert a product to a food_dict and
        return this dict. """

        dict = {}
        nutriscore_tab = ['A', 'B', 'C', 'D', 'E']

        dict['name'] = product['product_name']
        dict['nutriments'] = product['nutriments']
        dict['category_set'] = product['categories_tags']
        dict['img_front_url'] = product['image_front_thumb_url']
        dict['img_back_url'] = product['image_nutrition_thumb_url']
        dict['nutriscore'] = nutriscore_tab[product['nutriscore_data']['nutriscore_score']]

        return dict

    def set_product(self, product):

        try:
            self.dict = self._product_to_food_dict(product)
        except:
            pass


class OFFDatabase:

    def __init__(self):
        self.searchs = []

    def get_connexion(self):
        """ This method return if the openfoodfacts' server is up. """

        page = self._request()

        if True:
            return True
        else:
            return False

    def update_database(self, **kwargs):
        """ This method update the self.searchs after few minutes. """

        if kwargs.pop('test', False):
            self.searchs = self._fetch_categories(test=True)
        else:
            self.searchs = self._fetch_categories()

    def update_django(self):
        """ This method update django's database. """

        for search in self.searchs:

            try:
                food = Food.objects.get(name=product['name'])
                food.name = product['name']
                food.nutriments = product['nutriments']
                food.img_front_url = product['img_front_url']
                food.img_back_url = product['img_back_url']
                food.nutriscore = product['nutriscore']
            except:
                food = Food.objects.create(
                    name=product['name'],
                    nutriments=product['nutriments'],
                    img_front_url=product['img_front_url'],
                    img_back_url=product['img_back_url'],
                    nutriscore=product['nutriscore'],
                )

            for category_name in product['category_set']:
                try:
                    category = Category.objects.get(name=category_name, food_set__contains_id=food.id)
                except:
                    category = Category.objects.create(name=category_name)
                    food.category_set.add(category)


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

    def _fetch_categories(self, **kwargs):
        """ This private method perform all searchs. """

        is_test = kwargs.pop('test', False)

        categories = self._get_categories()

        page_size = 100

        if is_test:
            page_size = 10
            categories = ['Chocolat']

        for category in categories:
            beefeye = self._request(search=category)

            if is_test:
                beefeye['count'] = beefeye['count'] = 10

            number_of_pages = int(int(beefeye["count"]) / page_size)
            number_of_products = int(beefeye["count"])

            for page_index in range(number_of_pages):
                print('\nPage ' + str(page_index+1) + '/' + str(number_of_pages) + ' [search_terms=' + category + ']')
                page = self._request(page_size=page_size, page_index=page_index, search=category)

                for product_index in range(len(page['products'])):
                    product = page['products'][product_index]
                    print('Handling ' + product['product_name'])
                    category_index = page_index*page_size + product_index

                    off_search = OFFSearch(category_index, category, number_of_pages, number_of_products)
                    off_search.set_product(product)

                    print(off_search.dict)

                    if off_search.dict is not None:
                        self.searchs.append(off_search)


    def _search(self):
        """ This method make a search and return a json. """
        pass
