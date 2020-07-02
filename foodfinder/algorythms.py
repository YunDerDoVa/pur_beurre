from django.db.models import OuterRef, Subquery

from .models import Food
from favor.models import Favor

from datetime import datetime


class Algorythm:

    def __init__(self):
        pass

    def search_substitutes(self, food, account):
        """ This method search substitutes of a food and return a array of 6.
        Return None if no substitutes are found. """

        substitutes = []

        foods = self.get_queryset(food, account)

        for substitute in foods:

            if self.calcMatch(food, substitute):
                substitutes.append(substitute)

            if len(substitutes) >= 6:
                break

        return substitutes

    def get_queryset(self, food, account):

        foods = Food.objects.exclude(id=food.id)

        return foods

    def calcMatch(self, food, substitute):
        return False

    @staticmethod
    def get_algorythm_by_classname(classname):

        algorythms = {
            'ByCategory': ByCategory(),
        }

        return algorythms[classname]


class ByCategory(Algorythm):

    def get_queryset(self, food, account):

        foods = Food.objects.exclude(id=food.id)

        for category in food.category_set.all():
            new_foods = foods.filter(category_set__name__icontains=category.name)
            if new_foods.count() > 0:
                foods = new_foods

        return foods

    def calcMatch(self, food, substitute):

        good, bad = 0, 0

        for category in food.category_set.all():

            if category in substitute.category_set.all():
                good += 1
            else:
                bad += 1

        return good > bad
