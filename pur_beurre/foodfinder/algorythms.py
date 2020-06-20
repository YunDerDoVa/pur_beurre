from .models import Food


class Algorythm:

    def __init__(self):
        pass

    def search_substitutes(self, food):
        """ This method search substitutes of a food and return a array of 6.
        Return None if no substitutes are found. """

        substitutes = []

        for substitute in Food.objects.all():

            if self.calcMatch(food, substitute):
                substitutes.append(substitute)

            if len(substitutes) >= 6:
                break

        return substitutes

    def calcMatch(self, food, substitute):
        return False

    @staticmethod
    def get_algorythm_by_classname(classname):

        algorythms = {
            'ByFat': ByFat(),
            'BySalt': BySalt(),
            'ByNutriments': ByNutriments(),
            'ByCategory': ByCategory(),
            'ByFat': ByFat(),
        }

        return algorythms[classname]


class ByFat(Algorythm):

    def equation_result(self, fat_food, fat_substitute):

        return fat_food - fat_substitute

    def calcMatch(self, food, substitute):

        fat_food = food.food_nutriment_set.filter(nutriment__name='fat').first().quantity
        fat_substitute = substitute.food_nutriment_set.filter(nutriment__name='fat').first().quantity

        if fat_food is not None and fat_substitute is not None:

            if self.equation_result(fat_food, fat_substitute) < 1:
                return True
            else:
                return False

class BySalt(Algorythm):

    def equation_result(self, salt_food, salt_substitute):

        return salt_food - salt_substitute

    def calcMatch(self, food, substitute):

        salt_food = food.food_nutriment_set.filter(nutriment__name='salt').first().quantity
        salt_substitute = substitute.food_nutriment_set.filter(nutriment__name='salt').first().quantity

        if salt_food is not None and salt_substitute is not None:

            if self.equation_result(salt_food, salt_substitute) < 1:
                return True
            else:
                return False

class ByNutriments(Algorythm):

    def calcMatch(self, food, substitute):
        return True

class ByCategory(Algorythm):

    def calcMatch(self, food, substitute):

        good, bad = 0, 0

        for category in food.category_set.all():

            if category in substitute.category_set.all():
                good += 1
            else:
                bad += 1

        return good > bad
