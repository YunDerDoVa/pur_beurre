from django.test import TestCase

from django.urls import reverse


from mugauth.models import Account

# Create your tests here.
class MugauthViewsTestCase(TestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    def setUp(self):
        Account.objects.create_user(username=self.USERNAME, email=self.EMAIL, password=self.PASSWORD)

    def test_next_redirection(self):

        pass

#        url = reverse('login_view') + '?next=' + reverse('legacy')
#        data = {
#            'email': self.EMAIL,
#            'password': self.PASSWORD,
#        }

#        response = self.client.post(url, data, follow=False)

#        self.assertTemplateUsed(response, 'foodfinder/legacy.html.django')
