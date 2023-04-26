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



def validacao_campo(request,titulo,descricao,imagem):
    
    if not titulo.strip():
        messages.add_message(request, constants.ERROR, 'Campo titulo não pode ficar em branco!')
        return False
    if not descricao.strip():
        messages.add_message(request, constants.ERROR, 'Campo descrição não pode ficar em branco!')
        return False
    if not imagem.strip():
        messages.add_message(request, constants.ERROR, 'Campo imagem não pode ficar em branco!')
        return False
    
    return True


def validacao_campo_int(request,tempo, serve):
    
    if int(tempo) < 0 or int(serve) < 0:
        messages.add_message(request, constants.ERROR, 'Não pode haver valor negativo!')
        return False
    
    return True