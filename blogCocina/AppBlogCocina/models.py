from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=800)
    pasos_completos = models.CharField()
    imagen = models.ImageField(upload_to='imagenes_recetas', null=True, blank = True)


    def __str__(self):
        return f"Receta : {self.nombre} | descripcion: {self.descripcion}"
