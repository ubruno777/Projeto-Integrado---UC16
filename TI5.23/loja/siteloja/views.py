from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import criptografia
from .models import Clientes
import bcrypt

def cadCli(request):

    if request.method == 'POST':
        codcli = request.POST.get('codcli')
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        senhacripto = criptografia(senha)

        cliente = Clientes(
            codcli = codcli,
            nome = nome,
            cpf = cpf,
            email = email,
            senha = senhacripto
        )

        cliente.save()
        
        return render(request, 'formcli.html')

    return render(request, 'formcli.html')

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            cliente = Clientes.objects.get(email = email)
        except Clientes.DoesNotExist:
            messages.error(request, 'Usuario ou senha invalido')
            return render(request, 'login.html')
        
        if bcrypt.checkpw(senha.encode('utf-8'), cliente.senha.encode('utf-8')):
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou senha invalido')
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout(request):

    return

def home(request):

    return



