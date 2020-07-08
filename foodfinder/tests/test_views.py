from django.test import TestCase

from django.urls import reverse


from foodfinder.views import home
from foodfinder.models import Food, Category, Nutriment, FoodNutriment, FoodHistory
from mugauth.models import Account


class ViewsTestCase(TestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    VALID_DATA = {'search_term': 'chocolat'}
    NON_VALID_DATA = {'form': 'chocolat'}

    FOOD = {
        'code': '1024',
        'name': 'chocolat',
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

            food_nutriment = FoodNutriment.objects.create(
                food=food, nutriment=nutriment,
                quantity=nutriment_quantity)

    def test_home_template_used(self):

        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'foodfinder/home.html.django')

    def test_search_template_used(self):

        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.post(reverse('search'), {'search_term': 'chocolat'})

        self.assertTemplateUsed(response, 'foodfinder/results_page.html.django')

    def test_food_page_template_used(self):

        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('food_page', kwargs={'code': self.FOOD['code']}))

        self.assertTemplateUsed(response, 'foodfinder/food_page.html.django')

    def test_account_template_used(self):

        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('account_page'))

        self.assertTemplateUsed(response, 'foodfinder/account_page.html.django')

    def test_legacy_template_used(self):

        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get(reverse('legacy'))

        self.assertTemplateUsed(response, 'foodfinder/legacy.html.django')

    def test_search_perform_search_valid(self):

        url = reverse('search')
        data = self.VALID_DATA

        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        response = self.client.post(url, data, follow=False)

        self.assertEqual(response.status_code, 200)

    def test_search_perform_search_non_valid(self):

        url = reverse('search')
        data = self.NON_VALID_DATA

        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def test_search_in_history(self):

        self.account.allow_datashare = True
        self.account.save()

        url = reverse('search')
        data = self.VALID_DATA

        self.client.login(username=self.USERNAME, password=self.PASSWORD)

        response = self.client.post(url, data)

        history = FoodHistory.objects.filter(user=self.account).first()

        self.assertEqual(history.food.name, self.VALID_DATA['search_term'])



# assert code=200
# response.content : html
# response.context : context de render
# self.assertTemplateUsed : vérifie le bon template (!= ...NotUsed)
