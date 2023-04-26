from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Receita
from django.contrib import messages
from django.contrib.messages import constants


#jogar as receitas publicadas de quem ta logado na home, junto com as receitas padroes pre-cadastradas por nós
def home(request):
    return render(request,'home.html')
    

@login_required
def nova_receita(request):
    if request.method == 'GET':
        return render(request, 'nova_receita.html')
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        tempo_preparacao = request.POST.get('tempo_preparacao')
        serve_pessoas = request.POST.get('serve_pessoas')
        valor = request.POST.get('publicada')
        if valor == "True":
            publicada = True
        else:
            publicada = False
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
    return redirect('gerenciar_receitas')
    
    
    
@login_required   
def gerenciar_receitas(request):
    if request.method =='GET':
        receitas = Receita.objects.filter(autor=request.user.id)
        return render(request, 'gerenciar_receitas.html', {'receitas': receitas})
    
 
 # fazer os campos de imagem e publicada serem editados
@login_required  
def editar_receita(request,receita_id):
    receita = get_object_or_404(Receita,pk=receita_id)
    return render(request, 'editar.html', {'receita': receita })
 
 
@login_required   
def atualizar_receita(request, receita_id):
    receita = get_object_or_404(Receita,pk=receita_id)
    
    if request.method == 'POST':
        receita.titulo = request.POST['titulo']
        receita.descricao = request.POST['descricao']
        receita.tempo_preparacao = request.POST['tempo_preparacao']
        receita.serve_pessoas = request.POST['serve_pessoas']        
        receita.save()
        messages.add_message(request, constants.SUCCESS, 'Receita Atualizada!!!')
        return redirect('gerenciar_receitas')

def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita,pk=receita_id)
    receita.delete()
    return redirect('gerenciar_receitas')
