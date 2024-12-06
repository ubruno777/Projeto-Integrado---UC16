from django.urls import path
from django.shortcuts import render
from .views import cadCli, login, logout, home

urlpatterns = [
    path('', cadCli, name='formcli' ),
    path('login/', login, name='login'),
    path('logout/', logout, name='login'),
    path('home/', lambda request: render(request, 'home.html'), name='home' )
]