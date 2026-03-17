from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
