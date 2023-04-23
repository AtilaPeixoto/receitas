from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class Receita(admin.ModelAdmin):
    list_display = ['titulo', 'publicada', 'autor',]
