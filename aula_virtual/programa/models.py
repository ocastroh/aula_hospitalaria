from django.db import models

class ListaProgramaApoyo(models.Model):
    nombre = models.CharField(max_length=200,null=True)
    

class HojaDeVida(models.Model):
    promedio = models.FloatField()
    observacion = models.TextField()
    alumno = models.OneToOneField('personas.Alumno', on_delete=models.CASCADE)

