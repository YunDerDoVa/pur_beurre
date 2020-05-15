from django.test import TestCase
from django.test.client import RequestFactory

from django.contrib.auth.models import User

from foodfinder.models import Account
from foodfinder.algorythms.py import ByFat


# Create your tests here.
class AccountTestCase(TestCase):
    """ AccountTestCase test the Account system """

    USER = ('Test User 1', 'mail@mail.com', 'password')

    def setUp(self):
        """ Setting tests up """

        self.request_factory = RequestFactory()

        account = Account()
        self.account = account.create_account_and_user(self.USER[0], self.USER[1], self.USER[2])


    def test_create_account(self):
        """ Create Account """

        account = Account.objects.get(user__username=self.USER[0])

        self.assertEqual(account.user.username, self.USER[0])

    def test_authenticate(self):
        """ Authenticate Account """

        account = Account.authenticate(self.USER[1], self.USER[2])

        self.assertEqual(account.user.username, self.USER[0])

    def test_login(self):
        """ Login Account """

        request = self.request_factory.get('/login')
        self.account.login_account(request)

        self.assertEqual(request.user, self.account.user)

    def test_choose_algorythm(self):
        """ Choose Algorythm """

        ALGORYTHMS = ['BY_FAT', 'BY_SALT']

        algorythm = self.acount.get_search_algorythm()

        self.assertEqual(type(algorythm), type(ByFat()))
