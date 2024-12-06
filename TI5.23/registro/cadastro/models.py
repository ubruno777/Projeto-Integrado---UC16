from django.db import models

class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=250)
    cpf = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
