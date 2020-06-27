from django.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from datetime import date


from .managers import FoodManager


# Create your models here.
class SearchFoodRequests(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)

class SearchAlgorythm(models.Model):

    class AlgorythmChoices(models.TextChoices):

        BY_FAT = 'ByFat', _('By Fat')
        BY_SALT = 'BySalt', _('By Salt')
        BY_NUTRIMENTS = 'ByNutriments', _('By Nutriments')
        BY_CATEGORY = 'ByCategory', _('By Category')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    algorythm = models.CharField(
        max_length=63,
        choices=AlgorythmChoices.choices,
        default=AlgorythmChoices.BY_FAT,
    )

    def __str__(self):
        return self.algorythm + ' (' + self.user.username + ')'

class Food(models.Model):

    class NutriscoreChoices(models.TextChoices):

        A = 'A', 'A'
        B = 'B', 'B'
        C = 'C', 'C'
        D = 'D', 'D'
        E = 'E', 'E'

    code = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=127)
    img_front_url = models.URLField()
    img_back_url = models.URLField()
    nutriscore = models.CharField(max_length=7, choices=NutriscoreChoices.choices, default=None, null=True)
    update_date = models.DateField(auto_now=True)
    category_set = models.ManyToManyField('Category')
    objects = FoodManager()

    def __str__(self):
        return self.name + ' (code:' + self.code + ')'


class FoodNutriment(models.Model):

    food = models.ForeignKey('Food', on_delete=models.CASCADE, related_name='food_nutriment_set')
    nutriment = models.ForeignKey('Nutriment', on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.nutriment) + ' (' + str(self.quantity) + ')'


class Nutriment(models.Model):

    name = models.CharField(max_length=127, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name + ' (' + str(self.food_set.count()) + ' items)'
