from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_datashare = models.BooleanField(default=False)


class SearchFoodRequests(models.Model):

    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
