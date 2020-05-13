from django.urls import path

from . import views, auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', auth_views.register_view, name='register_view'),
    path('login/', auth_views.login_view, name='login_view'),
    path('logout/', auth_views.logout_view, name='logout_view'),
]
