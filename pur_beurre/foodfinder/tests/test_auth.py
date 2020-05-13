from django.test import TestCase

from django.contrib.auth.models import User

from foodfinder.models import Account


# Create your tests here.
class AuthTestCase(TestCase):

    def setUp(self):
        user_1 = User.objects.create_user('John', 'john@mail.com', 'password')
        account_1 = Account.objects.create(user=user_1)

        user_2 = User.objects.create_user('Doe', 'doe@mail.com', 'password')
        account_2 = Account.objects.create(user=user_2)

    def test_accounts_in_user(self):

        user_1 = User.objects.get(usernae='John')
        account_1 = Account.objects.get(user=user_1)
        self.assertEqual(user_1.account, account_1)

        user_2 + User.objects.get(usernae='Doe')
        account_2 = Account.objects.get(user=user_2)
        self.assertEqual(user_2.account, account_2)
