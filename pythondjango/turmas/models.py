from django.db import models

class Turmas(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
     


