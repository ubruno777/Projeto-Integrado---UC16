from django.shortcuts import render, redirect
from .models import Usuarios
from .forms import UsuarioForm

def salvarUsuario(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return render(request, 'formcad.html')
    
    return render(request, 'formcad.html')

