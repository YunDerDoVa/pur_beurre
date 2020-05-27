from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Account(AbstractUser):

    class SearchingAlgorythm(models.TextChoices):

        BY_FAT = 'ByFat', _('By Fat')
        BY_SALT = 'BySalt', _('By Salt')
        BY_NUTRIMENTS = 'ByNutriments', _('By Nutriments')
        BY_CATEGORY = 'ByCategory', _('By Category')

    allow_datashare = models.BooleanField(default=False)
    search_algorythm = models.CharField(
        max_length=63,
        choices=SearchingAlgorythm.choices,
        default=SearchingAlgorythm.BY_FAT,
    )

    def __str__(self):
        return str(self.user)
