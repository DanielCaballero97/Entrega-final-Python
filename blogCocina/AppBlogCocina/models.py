from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Receta(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=800)
    pasos_completos = models.CharField(max_length=8000)
    categoria = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return f"Receta : {self.nombre} | descripcion: {self.descripcion}"

class Image(models.Model):
    receta = models.ForeignKey(Receta, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Receta-imagenes/')