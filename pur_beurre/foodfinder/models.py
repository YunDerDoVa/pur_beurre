from django.db import models

from django.conf import settings


# Create your models here.
class SearchFoodRequests(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
