from django.shortcuts import render, redirect
from .models import CheckUser
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout

def login_user(request):
    if request.method == 'POST':
        usercheck = request.POST['userid']
        passwordcheck = request.POST['password']

        try:
            userok = CheckUser.objects.get(userid=usercheck, password=passwordcheck)
            request.session['user_loged'] = userok.id
            request.session['user_name'] = userok.userid
            return redirect('home')
        except CheckUser.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválida')

    return render(request, 'index.html')

def home_user(request):
    if 'user_loged' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('index')
        
