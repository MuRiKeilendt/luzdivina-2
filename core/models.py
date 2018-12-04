from django.db import models

# Create your models here.


class Comunidad(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Comunidadcatolica(models.Model):
    NombreComunidad = models.CharField(max_length=45)

    def __str__(self):
        return self.NombreComunidad


class Bautizo(models.Model):
    bautizado = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    padrino = models.CharField(max_length=45)
    madrina = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.bautizado


class Boda(models.Model):
    nombreNovia = models.CharField(max_length=45)
    nombreNovio = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreNovia


class Comunion(models.Model):
    nombreComunion = models.CharField(max_length=45)
    edad = models.CharField(max_length=45)
    numeroContacto = models.CharField(max_length=45)
    emailContacto = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    tipoParroquia = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComunion