from django.test import TestCase


from foodfinder.models import Food, Category, Nutriment, FoodNutriment


class ModelsTestCase(TestCase):

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

            food_nutriment = FoodNutriment.objects.create(
                food=food, nutriment=nutriment,
                quantity=nutriment_quantity)

    def test_models_relations(self):

        food = Food.objects.filter(name='TestFood').first()

        category = food.category_set.filter(name=self.FOOD['categories'][0]).first()

        food_nutriment = food.food_nutriment_set.filter(nutriment__name='fat').first()

        self.assertEqual(food.code, self.FOOD['code'])
        self.assertEqual(category.name, self.FOOD['categories'][0])
        self.assertEqual(
            (food_nutriment.food.name, food_nutriment.quantity),
            (self.FOOD['name'], self.FOOD['nutriments']['fat'])
        )

    def test_food(self):

        food = Food.objects.filter(name=self.FOOD['name']).first()

        self.assertEqual(food.name, self.FOOD['name'])
        self.assertEqual(food.code, self.FOOD['code'])
        self.assertEqual(food.img_front_url, self.FOOD['img_front_url'])
        self.assertEqual(food.img_back_url, self.FOOD['img_back_url'])
        self.assertEqual(food.nutriscore, self.FOOD['nutriscore'])
        self.assertTrue(food.category_set.first().name in self.FOOD['categories'])
        self.assertEqual(food.food_nutriment_set.get(food=food, nutriment__name='fat').quantity, self.FOOD['nutriments']['fat'])
