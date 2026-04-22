from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('login_user', views.login_user, name='login_user'),
]
