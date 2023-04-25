from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Receita
from django.contrib import messages
from django.contrib.messages import constants


@login_required
def nova_receita(request):
    if request.method == 'GET':
        return render(request, 'nova_receita.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descrição')
        tempo_preparacao = request.POST.get('tempo_preparacao')
        serve_pessoas = request.POST.get('serve_pessoas')
        publicada = request.POST.get('publicada')
        imagem = request.POST.get('imagem')
        
    receita = Receita(
        autor=request.user,
        titulo=titulo,
        descricao=descricao,
        tempo_preparacao=tempo_preparacao,
        serve_pessoas=serve_pessoas,
        publicada=publicada,
        imagem=imagem,
    )
    
    receita.save()
    
    messages.add_message(request, constants.SUCCESS, 'Receita cadastrada com sucesso!!!')
    return redirect('nova_receita')
    
    
    
@login_required   
def gerenciar_receitas(request):
    """_summary_ Busca das receitas cadastradas pelo usuario logado. poderá alterar e excluir

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_ pagina HTML com as receitas do usuario logado 
    """
    if request.method =='GET':
        titulo = request.GET.get('titulo')
        receitas = Receita.objects.all()
        filter(autor=request.user)
        
        if titulo:
            receitas = receitas.filter(titulo__contains=titulo)
        return render(request, 'gerenciar_receita.html', {'receitas': receitas})
    
    
    
def escolha_receita(request):
    """_summary_objetivo buscar receitas de todos os usuarios para a escolha da que agradar. 
    nao deve dar o direito de alterar ou excluir apenas vizualizar

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_pagina HTML com as receitas de nome equivalente para VISUALIZAÇÃO
    """
    if request.method == 'GET':
        titulo = request.GET.get('titulo')
        receitas = Receita.objects.all()
        
        if titulo:
            receitas = receitas.filter(titulo__constants=titulo)
        # return render(request, 'escolha_receita.html, {'receitas': receitas})
        return HttpResponse("escolha_receita")
