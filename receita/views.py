from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Receita
from django.contrib import messages
from django.contrib.messages import constants
from usuarios.utils import validacao_campo, validacao_campo_int, validacao_img



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
        publicada = request.POST.get('publicada')       
        imagem = request.POST.get('imagem')
        
        if not validacao_campo_int(request, tempo_preparacao, serve_pessoas):      
            return redirect('nova_receita')  
        if not validacao_campo(request,titulo, descricao, imagem):
            return redirect('nova_receita')
        
        try:
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
        except:
            messages.add_message(request, constants.ERROR, 'Alguma opção de publicar deve ser escolhida!')
            return redirect('nova_receita')
        
        messages.add_message(request, constants.SUCCESS, 'Receita cadastrada com sucesso!!!')
        return redirect('gerenciar_receitas')
    
    
    
@login_required   
def gerenciar_receitas(request):
    if request.method =='GET':
        receitas = Receita.objects.filter(autor=request.user.id)
        return render(request, 'gerenciar_receitas.html', {'receitas': receitas})
    
 
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
        receita.publicada = request.POST['publicada']   
        imagem = request.POST['imagem']
         
        if validacao_img(imagem):
              receita.imagem = imagem 
              
        receita.save()
        messages.add_message(request, constants.SUCCESS, 'Receita Atualizada!!!')
        return redirect('gerenciar_receitas')

@login_required  
def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receita,pk=receita_id)
    receita.delete()
    messages.add_message(request, constants.INFO, 'Receita Deletada!')
    return redirect('gerenciar_receitas')


'''def escolha_receita(request):
    return HttpResponse('Escolha')

    if request.method == 'GET':
        titulo = request.GET.get('titulo')
        receitas = Receita.objects.all()

        if titulo:
            receitas = receitas.filter(titulo__constants=titulo)
        # return render(request, 'escolha_receita.html, {'receitas': receitas})
        return HttpResponse("escolha_receita") '''