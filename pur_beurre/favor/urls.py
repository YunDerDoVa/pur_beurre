from django.urls import path

from . import views

urlpatterns = [
    path('', views.favors, name='favors'),
    path('add_favor/<int:food_code>/', views.add_favor, name='add_favor'),
]
