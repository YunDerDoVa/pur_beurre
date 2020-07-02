from django.urls import path

from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    #path('login/', auth_views.LoginView.as_view(template_name='auth/login.html.django'), name='login_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
]
