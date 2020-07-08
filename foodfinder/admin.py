from django.contrib import admin

from .models import FoodHistory, Food, Category, Nutriment, FoodNutriment


# Register your models here.
admin.site.register(FoodHistory)

admin.site.register(Food)

admin.site.register(Category)

admin.site.register(Nutriment)

admin.site.register(FoodNutriment)
