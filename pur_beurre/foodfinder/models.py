from django.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SearchFoodRequests(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    search = models.CharField(max_length=255)
    #food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)

class SearchAlgorythm(models.Model):

    class AlgorythmMChoice(models.TextChoices):

        BY_FAT = 'ByFat', _('By Fat')
        BY_SALT = 'BySalt', _('By Salt')
        BY_NUTRIMENTS = 'ByNutriments', _('By Nutriments')
        BY_CATEGORY = 'ByCategory', _('By Category')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    algorythm = models.CharField(
        max_length=63,
        choices=AlgorythmMChoice.choices,
        default=AlgorythmMChoice.BY_FAT,
    )
