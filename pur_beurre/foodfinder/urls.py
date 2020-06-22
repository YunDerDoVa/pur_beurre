from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('food/<int:code>/', views.food_page, name='food_page'),
    path('account/', views.account_page, name='account_page'),
]
