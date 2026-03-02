from django.db import models
from cloudinary.models import CloudinaryField

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    endereco = models.TextField(help_text="Endereço em Barra Velha")
    ponto_referencia = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    litragem = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = CloudinaryField('imagem', folder='barrachopp/produtos') 
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - {self.litragem}L"

class Chopeira(models.Model):
    STATUS_CHOICES = [('GALPAO', 'No Galpão'), ('CLIENTE', 'Com Cliente'), ('MANUTENCAO', 'Manutenção')]
    identificacao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=[('GELO', 'A Gelo'), ('ELETRICA', 'Elétrica')])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='GALPAO')

    def __str__(self):
        return f"{self.identificacao} ({self.status})"