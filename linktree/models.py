from django.db import models

# Create your models here.

class Link(models.Model):
    class Owner(models.TextChoices):
        IMOBILIARIA = 'IMOBILIARIA'
        CONSTRUTORA = 'CONSTRUTORA'

    text = models.CharField(max_length=255)
    href = models.CharField(max_length=255)
    owner = models.CharField(max_length=50,choices=Owner.choices,default='')
    
    