from django.contrib import admin

from .models import SearchFoodRequests, Food, Category, Nutriment


# Register your models here.
admin.site.register(SearchFoodRequests)

admin.site.register(Food)

admin.site.register(Category)

admin.site.register(Nutriment)
