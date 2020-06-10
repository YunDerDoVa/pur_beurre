from django.test import TestCase

from django.conf import settings
from django.contrib.auth import login, authenticate, logout

from mugauth.models import Account

# Create your tests here.
class AccountTestCase(TestCase):

    USERNAME = 'TestUser'
    EMAIL = 'test@email.com'
    PASSWORD = 'password'

    def setUp(self):
        Account.objects.create_user(username=self.USERNAME, email='test@email.com', password='password')

    def test_auth_user_model(self):
        model = settings.AUTH_USER_MODEL
        self.assertEqual(model, 'mugauth.Account')

    def test_authenticate(self):
        account = authenticate(username=self.USERNAME, password=self.PASSWORD)
        self.assertEqual(account.username, self.USERNAME)

    def test_fields(self):
        pass
