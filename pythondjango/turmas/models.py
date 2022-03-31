from django.db import models
from django.contrib.auth import get_user_model

class Turmas(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
    matricula = models.ManyToManyField(get_user_model()) 

    

