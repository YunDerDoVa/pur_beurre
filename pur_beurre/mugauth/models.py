from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Account(AbstractUser):

    allow_datashare = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)
