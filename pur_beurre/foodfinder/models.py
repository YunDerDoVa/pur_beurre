from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.utils.translation import gettext_lazy as _


# Create your models here.
class Account(models.Model):

    class SearchingAlgorythm(models.TextChoices):

        BY_FAT = 'ByFat', _('By Fat')
        BY_SALT = 'BySalt', _('By Salt')
        BY_NUTRIMENTS = 'ByNutriments', _('By Nutriments')
        BY_CATEGORY = 'ByCategory', _('By Category')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_datashare = models.BooleanField(default=False)
    search_algorythm = models.CharField(
        max_length=63,
        choices=SearchingAlgorythm.choices,
        default=SearchingAlgorythm.BY_FAT,
    )


    @staticmethod
    def authenticate(email, password):

        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)
        except:
            user = authenticate(username=email, password=password)

        if user:
            account = Account.objects.get(user=user)
            return account

        return None

    def create_account_and_user(self, name, email, password):

        self.user = User.objects.create_user(name, email, password)
        self.save()

        return self

    def login_account(self, request):

        login(request, self.user)

    def __str__(self):
        return str(self.user)


class SearchFoodRequests(models.Model):

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
