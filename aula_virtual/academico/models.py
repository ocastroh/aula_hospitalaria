from django.db import models

class TipoClase(models.Model):
    nombre = models.CharField(max_length=100)

class Clase(models.Model):
    tipo = models.ForeignKey(TipoClase, on_delete=models.PROTECT)
    hr_inicio_programado = models.TimeField()
    hr_termino_programado = models.TimeField()
    hr_inicio_efectivo = models.TimeField(null=True, blank=True)
    hr_termino_efectivo = models.TimeField(null=True, blank=True)
    duracion_clase = models.DurationField()

class Curso(models.Model):
    grado = models.CharField(max_length=50)
    identificador = models.CharField(max_length=100)

class Asignatura(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    docente = models.ForeignKey('personas.Docente', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    

class Material(models.Model):
    titulo = models.CharField(max_length=200)
    ruta_directorio = models.CharField(max_length=500)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

class CalificacionDocente(models.Model):
    calificacion = models.FloatField()