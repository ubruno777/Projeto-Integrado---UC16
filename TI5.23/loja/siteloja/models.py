from django.db import models

class Clientes(models.Model):

    codcli = models.CharField(max_length=7, unique=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12)
    email = models.EmailField(max_length=200)
    senha = models.CharField(max_length=250)

    def __str__(self):
        return self.codcli
    
class Pedido(models.Model):

    numero = models.IntegerField()
    total = models.DecimalField(decimal_places=2,max_digits=8)
    entrega = models.CharField(max_length=250)
    codcli = models.ForeignKey(Clientes,on_delete=models.PROTECT)

    def __str__(self):
        return self.numero