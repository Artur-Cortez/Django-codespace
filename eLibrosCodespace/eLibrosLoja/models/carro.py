from django.db import models

class Carro(models.Model):
    cor = models.CharField(max_length=6)
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(decimal_places=2, max_digits=8)
    numero_portas = models.IntegerField()
