from django.db import models

from django.conf import settings


from foodfinder.models import Food


# Create your models here.
class Favor(models.Model):

    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    substitute_of = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='substitute_of_set')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return food.name + ' (' + self.account.username + ')'
