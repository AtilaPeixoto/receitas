from django.urls import path
from . import views


urlpatterns = [
    path('escolha_receita', views.escolha_receita, name='escolha_receita' ),
    path('nova_receita', views.nova_receita, name='nova_receita' ),
    path('gerenciar_receitas', views.gerenciar_receitas, name='gerenciar_receitas' ),

]