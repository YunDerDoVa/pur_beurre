from django.test import TestCase


from .models import Food, Category, Nutriments


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
        pass

    def test_models_relations(self):

        food = Food.objects.create(
            name=self.FOOD['name'],
            code=self.FOOD['code'],
            img_front_url=self.FOOD['img_front_url'],
            img_back_url=self.FOOD['img_back_url'],
            nutriscore=self.FOOD['nutriscore'])

        for category_name in self.FOOD['categories']:
            category = Category.objects.create(name=category_name)

        for nutriment_name, nutriment_quantity in self.FOOD['nutriments']:
            nutriment = Nutriment.objects.create(name=nutriment_name)
            food_nutriment = FoodNutriment.objects.create(
                food=food, nutriment=nutriment,
                quantity=nutriment_quantity)
