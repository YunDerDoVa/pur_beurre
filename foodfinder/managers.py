from django.db import models


class FoodManager(models.Manager):

    def get_food_by_search_term(self, search_term):

        food = self.filter(name__iexact=search_term).first()

        if food is None:
            food = self.filter(name__icontains=search_term).first()

            if food is None:
                splited_search_term = search_term.split(' ')

                foods = None

                for term in splited_search_term:
                    if foods is None:
                        foods = self.filter(name__icontains=term)
                    else:
                        intersection = foods.intersection(self.filter(name__icontains=term))
                        if intersection.count() > 0:
                            foods = intersection

                    food = foods.first()

        return food
