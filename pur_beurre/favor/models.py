from django.db import models

from django.conf import settings


from foodfinder.models import Food


# Create your models here.
class Favor(models.Model):

    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return food.name + ' (' + self.account.username + ')'
