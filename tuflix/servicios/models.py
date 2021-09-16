from django.db import models

# Create your models here.
class Musico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    salario = models.IntegerField()

    def __str__(self):
        return self.nombre


class Album(models.Model):
    musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    fecha_pub = models.DateField()
    caratula = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    duracion = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.nombre