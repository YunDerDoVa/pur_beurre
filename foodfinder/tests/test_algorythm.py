from django.test import TestCase


from foodfinder.algorythms import Algorythm
from foodfinder.models import Food, Category, Nutriment, FoodNutriment
from mugauth.models import Account


class AlgorythmTestCase(TestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    FOOD = {
        'code': '1024',
        'name': 'TestFood',
        'img_front_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'img_back_url': 'https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg',
        'nutriscore': 'A',
        'nutriments': {'fat': 1.2, 'salt': 2.4},
        'categories': ['Chocolat', 'Sugar'],
    }

    def setUp(self):

        self.account = Account.objects.create_user(username=self.USERNAME, email=self.EMAIL, password=self.PASSWORD)

        food = Food.objects.create(
            name=self.FOOD['name'],
            code=self.FOOD['code'],
            img_front_url=self.FOOD['img_front_url'],
            img_back_url=self.FOOD['img_back_url'],
            nutriscore=self.FOOD['nutriscore'])

        for category_name in self.FOOD['categories']:
            category = Category.objects.create(name=category_name)
            food.category_set.add(category)

        for nutriment_name, nutriment_quantity in self.FOOD['nutriments'].items():
            nutriment = Nutriment.objects.create(name=nutriment_name)
            food_nutriment = FoodNutriment.objects.create(food=food, nutriment=nutriment, quantity=nutriment_quantity)
            food.food_nutriment_set.add(food_nutriment)

    def test_search_substitutes_by_category(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()
        algorythm = Algorythm.get_algorythm_by_classname('ByCategory')
        substitutes = algorythm.search_substitutes(food, self.account)

        self.assertEqual(type(substitutes), type([None]))
