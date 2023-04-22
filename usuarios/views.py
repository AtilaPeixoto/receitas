from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('senha').strip()
        confirmar_senha = request.POST.get('confirmar_senha').strip()
        
        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas nao conferem.')
            return redirect('login')

        user = User.objects.filter(username=name)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario ja existe')
            return redirect('cadastro')   
        
        try:
            user = User.objects.create_user(username=name, email=email, password=senha)
             
            messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')
            return render(request, 'login.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno. Tente novamente.')
            return render(request, 'cadastro.html')
         
    
    
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        name = request.POST.get('name').strip()
        senha = request.POST.get('senha').strip()
        
        user = auth.authenticate(username=name, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Nome de usuario e ou senha invalidos')
            return redirect('login')
        
        
        auth.login(request, user)
        return HttpResponse('estou logado')
    
    
def sair(request):
    auth.logout(request)
    return HttpResponse('vc saiu')