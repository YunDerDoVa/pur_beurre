from django.test import TestCase

from django.urls import reverse


from foodfinder.views import home


class ViewsTestCase(TestCase):

    VALID_DATA = {'search_term': 'chocolat'}
    NON_VALID_DATA = {'form': 'chocolat'}

    def setUp(self):
        pass

    def test_home_template_used(self):

        response = self.client.get(reverse('home'))

        self.assertTemplateUsed(response, 'foodfinder/home.html.django')

    def test_search_perform_search_valid(self):

        url = reverse('search')

        data = self.VALID_DATA

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def test_search_perform_search_non_valid(self):

        url = reverse('search')

        data = self.NON_VALID_DATA

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)


# assert code=200
# response.content : html
# response.context : context de render
# self.assertTemplateUsed : vérifie le bon template (!= ...NotUsed)
