from django.urls import path

from . import views

urlpatterns = [
    path('foodname/', views.foodname, name='autocomplete_foodname'),
]
