from django.test import TestCase

from unittest.mock import MagicMock, create_autospec


from filler.openfoodfacts.database import OFFDatabase, OFFSearch
from foodfinder.models import Food


# Create your tests here.
class OpenFoodFactsTestCase(TestCase):

    PRODUCT = {
        'product_name': 'TestFood',
        'code': '1024',
        'nutriments': {'fat': 1.2},
        'categories_tags': ['Chocolat', 'Sugar'],
        'image_front_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'image_nutrition_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore_grade': 'a',
    }
    PRODUCT_2 = {
        'product_name': 'TestFood',
        'code': '1025',
        'nutriments': {'fat': 1.2},
        'categories_tags': ['Chocolat', 'Sugar'],
        'image_front_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'image_nutrition_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore_grade': 'a',
    }
    PRODUCT_3 = {
        'product_name': 'TestFood',
        'code': '1026',
        'nutriments': {'fat': 1.2},
        'categories_tags': ['Chocolat', 'Sugar'],
        'image_front_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'image_nutrition_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore_grade': 'a',
    }
    PRODUCT_4 = {
        'product_name': 'TestFood',
        'code': '1027',
        'nutriments': {'fat': 1.2},
        'categories_tags': ['Chocolat', 'Sugar'],
        'image_front_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'image_nutrition_thumb_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore_grade': 'a',
    }
    PRODUCT_SET = [PRODUCT, PRODUCT_2, PRODUCT_3]
    PAGE = {
        'products': PRODUCT_SET,
        'count': 3,
    }

    def setUp(self):

        self.SEARCHS = []
        forloop = 0

        for product in self.PRODUCT_SET:
            search = OFFSearch(forloop, 'Test', 1, 1)
            search.set_product(product)

            self.SEARCHS.append(search)
            forloop += 1

        self.database = OFFDatabase()

    def test_update_database(self):

        self.database._request = MagicMock(return_value=self.PAGE)
        self.database.update_database(test=True)

        self.assertEqual(len(self.database.searchs), 3)

    def test_update_django(self):

        self.database._request = MagicMock(return_value=self.PAGE)
        self.database.update_database(test=True)
        self.database.update_django()

        query = Food.objects.filter(name='TestFood')
        self.assertEqual(len(self.SEARCHS), len(query))
