from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('food/<int:code>/', views.food_page, name='food_page'),
    path('account/', views.account_page, name='account_page'),
    path('legacy/', views.legacy, name='legacy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
