from django.urls import path
from .views import login_user, home_user, logout_user

urlpatterns = [
    path('', login_user, name='index'),
    path('home/', home_user, name='home'),
]