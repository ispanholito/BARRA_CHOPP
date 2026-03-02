from django.contrib import admin
from .models import Cliente, Produto, Chopeira

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'bairro', 'whatsapp')
    search_fields = ('nome', 'whatsapp')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'litragem', 'preco', 'ativo')

@admin.register(Chopeira)
class ChopeiraAdmin(admin.ModelAdmin):
    list_display = ('identificacao', 'tipo', 'status')
    list_filter = ('status', 'tipo')