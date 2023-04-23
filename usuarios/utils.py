from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User

#validaçao de senhas em função especifica para isso
# depois podemos validar senhas q tenham mais caracteres, com mistura de letras e numeros.

def validacao(request, senha, confirmar_senha):
    
        if senha and len(senha) < 5:
            messages.add_message(request, constants.ERROR, 'A senha é muito pequena.')
            return False
        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas não conferem.')
            return False 
        
        return True