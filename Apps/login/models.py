from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    tipo = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
