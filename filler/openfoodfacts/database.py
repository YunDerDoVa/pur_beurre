import json
import requests


from foodfinder.models import Food, Category, Nutriment, FoodNutriment


class OFFSearch:

    def __init__(self, category_index, category, pages, products):

        self.category_index = category_index
        self.category = category
        self.number_of_pages = pages
        self.number_of_products = products
        self.dict = {}

    def _product_to_food_dict(self, product):
        """ This method convert a product to a food_dict and
        return this dict. """

        dict = {}

        dict['code'] = product['code']
        dict['name'] = product['product_name']
        dict['nutriment_set'] = {
            'sugar': product['nutriments'].pop('sugars_100g', None),
            'salt': product['nutriments'].pop('salt_100g', None),
            'vitamin-a': product['nutriments'].pop('vitamin-a_100g', None),
            'vitamin-c': product['nutriments'].pop('vitamin-c_100g', None),
            'energy': product['nutriments'].pop('energy_100g', None),
            'fat': product['nutriments'].pop('fat_100g', None),
            'iron': product['nutriments'].pop('iron_100g', None),
            'calcium': product['nutriments'].pop('calcium_100g', None),
            'sodium': product['nutriments'].pop('sodium_100g', None),
            'proteins': product['nutriments'].pop('proteins_100g', None),
            'cholesterol': product['nutriments'].pop('cholesterol_100g', None),
            'carbohydrates': product['nutriments'].pop('carbohydrates_100g', None),
        }
        dict['category_set'] = product['categories_tags']
        dict['img_front_url'] = product['image_url']
        dict['img_back_url'] = product['image_nutrition_url']
        dict['nutriscore'] = product['nutriscore_grade'].upper()

        return dict

    def set_product(self, product):
        """ This method set the product in self.dict variable and return
        True if it's a success, False otherwise. """

        try:
            self.dict = self._product_to_food_dict(product)
            return True
        except:
            return False

    def __str__(self):
        return '<class: OFFSearch>, ' + str(self.category) + ' : ' + str(self.category_index + 1) + '/' + str(self.number_of_products)


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
            self._fetch_categories(test=True)
        else:
            self._fetch_categories()

    def update_django(self):
        """ This method update django's database. """

        print('\nUpdating Django... (' + str(len(self.searchs)) + ' items)')

        for search in self.searchs:

            food = Food.objects.filter(code=search.dict['code']).first()

            # Get or Create Food
            if food != None:
                food.name = search.dict['name']
                food.img_front_url = search.dict['img_front_url']
                food.img_back_url = search.dict['img_back_url']
                food.nutriscore = search.dict['nutriscore']
                food.save()
            else:
                food = Food.objects.create(
                    code=search.dict['code'],
                    name=search.dict['name'],
                    img_front_url=search.dict['img_front_url'],
                    img_back_url=search.dict['img_back_url'],
                    nutriscore=search.dict['nutriscore'],
                )

            # Get or Create Category
            for category_name in search.dict['category_set']:

                category = Category.objects.filter(name=category_name).first()
                if category == None:
                    category = Category.objects.create(name=category_name)

                if category not in food.category_set.all():
                    food.category_set.add(category)

            # Get or Create Nutriment and Attach to Food
            for nutriment_name, nutriment_quantity in search.dict['nutriment_set'].items():

                if nutriment_quantity is not None:
                    try:
                        nutriment = Nutriment.objects.filter(name=nutriment_name).first()
                        if nutriment == None:
                            nutriment = Nutriment.objects.create(name=nutriment_name)

                        # Attach Nutriment to Food
                        food_nutriment = FoodNutriment.objects.filter(nutriment=nutriment, food=food).first()
                        if food_nutriment == None:
                            food_nutriment = FoodNutriment.objects.create(
                                nutriment=nutriment, food=food,
                                quantity=nutriment_quantity)
                        else:
                            food_nutriment.quantity = nutriment_quantity
                            food_nutriment.save()

                        #print('\t-\t-\t' + 'Nutriment added')
                    except:
                        pass
                        #print('\t-\t-\t' + 'Nutriment not allowed')

            # Save Food
            food.save()

            if search.category_index%100 == 0:
                print('\t-\t' + str(search))


    def drop_django(self):
        """ This method drop django database """

        Food.objects.all().delete()
        Category.objects.all().delete()
        Nutriment.objects.all().delete()


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

        page_size = 1000
        categories = self._get_categories(['fruits', 'viandes', 'boissons'])

        if is_test:
            page_size = 3
            categories = ['Chocolat']

        for category in categories:
            beefeye = self._request(search=category)

            if is_test:
                beefeye['count'] = 3
            else:
                if int(beefeye['count']) > 2000:
                    beefeye['count'] = 2000

            number_of_pages = int(int(beefeye["count"]) / page_size)
            number_of_products = int(beefeye["count"])

            for page_index in range(number_of_pages):
                print('\nPage ' + str(page_index+1) + '/' + str(number_of_pages) + ' [search_terms=' + category + ']')
                page = self._request(page_size=page_size, page_index=page_index, search=category)

                for product_index in range(len(page['products'])):
                    product = page['products'][product_index]
                    #print('\t-\tHandling ' + product['product_name'])
                    category_index = page_index*page_size + product_index

                    off_search = OFFSearch(category_index, category, number_of_pages, number_of_products)

                    #print('\t-\t' + 'OFFSearch : ' +  str(off_search))

                    if off_search.set_product(product):
                        self.searchs.append(off_search)
                        #print('\t-\t' + 'In self.searchs')
                    #else:
                    #    print('\t-\t' + 'Error while setting product')

                    #print('\n')

                print('\t\t' + str(len(self.searchs)) + ' items')


    def _search(self):
        """ This method make a search and return a json. """
        pass
