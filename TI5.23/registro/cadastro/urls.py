from django.urls import path
from .views import salvarUsuario

urlpatterns = [
    path('', salvarUsuario, name='usuarioForm')
]