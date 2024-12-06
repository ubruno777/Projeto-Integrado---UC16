from django.db import models

class Product(models.Model):
    codprod = models.AutoField(primary_key=True)
    nameprod = models.CharField(max_length= 100)
    #Categoria do produto
    categoryprod =  models.CharField(max_length= 100)
    #Descrição do produto
    descprod = models.TextField()
    # marca do produto
    brandprod = models.CharField(max_length = 50)
    # Data de manufatura / produção
    manudateprod = models.DateField()
    weightprod = models.DecimalField(max_digits = 6, decimal_places = 2)
    
class  PriceProd(models.Model):
    codprice = models.AutoField(primary_key=True)
    #chave estrangeira que vai referenciar a table product
    codprod = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'codigo')
    #preço do produto
    priceprod = models.DecimalField(max_digits= 8, decimal_places= 2)
    #data de verificação
    dateverify = models.DateField()