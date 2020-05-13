from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your models here.
class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_datashare = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


class SearchFoodRequests(models.Model):

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
