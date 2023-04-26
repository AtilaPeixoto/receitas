from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('nova_receita', views.nova_receita, name='nova_receita' ),
    path('gerenciar_receitas', views.gerenciar_receitas, name='gerenciar_receitas' ),
    path('editar_receita/<int:receita_id>', views.editar_receita, name='editar_receita' ),
    path('atualizar_receita/<int:receita_id>', views.atualizar_receita, name='atualizar_receita' ),
    path('deletar_receita/<int:receita_id>', views.deletar_receita, name='deletar_receita' ),
    #path('escolha_receita', views.escolha_receita, name='escolha_receita' ),

]