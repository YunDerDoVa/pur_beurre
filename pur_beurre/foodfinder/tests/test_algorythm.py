from django.test import TestCase


from foodfinder.algorythms import Algorythm
from foodfinder.models import Food, Category, Nutriment, FoodNutriment


class AlgorythmTestCase(TestCase):

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

    def test_search_substitutes_by_fat(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()
        algorythm = Algorythm.get_algorythm_by_classname('ByFat')
        substitutes = algorythm.search_substitutes(food)

        self.assertEqual(substitutes[0].__class__, food.__class__)

    def test_search_substitutes_by_salt(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()
        algorythm = Algorythm.get_algorythm_by_classname('BySalt')
        substitutes = algorythm.search_substitutes(food)

        self.assertEqual(substitutes[0].__class__, food.__class__)

    def test_search_substitutes_by_nutriments(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()
        algorythm = Algorythm.get_algorythm_by_classname('ByNutriments')
        substitutes = algorythm.search_substitutes(food)

        self.assertEqual(substitutes[0].__class__, food.__class__)

    def test_search_substitutes_by_category(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()
        algorythm = Algorythm.get_algorythm_by_classname('ByCategory')
        substitutes = algorythm.search_substitutes(food)

        self.assertEqual(substitutes[0].__class__, food.__class__)
