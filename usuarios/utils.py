from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User

#validaçao de senhas em função especifica para isso
# depois podemos validar senhas q tenham mais caracteres, com mistura de letras e numeros.

def validacao(request, senha, confirmar_senha):
    
        if senha and len(senha) < 5:
            messages.add_message(request, constants.ERROR, 'Curto assi só se for o tempo de preparo.\nA senha é muito pequena.')
            return False
        if not (senha == confirmar_senha):
            messages.add_message(request, constants.ERROR, 'As senhas não conferem.')
            return False 
        
        return True



def validacao_campo(request, titulo, descricao, imagem):
    
    if not titulo.strip():
        messages.add_message(request, constants.ERROR, 'Eu gosto de ssaber oque vou comer, você não? Preencha o NOME DA RECEITA!')
        return False
    if not descricao.strip():
        messages.add_message(request, constants.ERROR, 'Ora este site depende deste campo, preencha a DESCRIÇÃO!')
        return False
    if not imagem.strip():
        messages.add_message(request, constants.ERROR, 'Você nunca comeu com os olhos?\n Nos mostre como é este prato, PONHA UMA FOTO!')
        return False
    
    return True


def validacao_campo_int(request, tempo, serve):
    
    if int(tempo) < 0:
        messages.add_message(request, constants.ERROR, 'Com tempo de preparo ZERO?! Essa receita eu preciso aprender!\n Por favor coloque o tempo de preparo.')
        return False
    if int(serve) < 0:
        messages.add_message(request, constants.ERROR, 'Ao menos uma possoa precisa comer!\n Por favor indique um numero de refeições da porção.')
    
    return True

def validacao_img(campo):
    
     if not campo.strip():
         return False
     
     return True