from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    
        
class Matricula(models.Model):
    folio = models.CharField(max_length=50)
    fecha = models.DateField()
    observaciones = models.TextField()
    sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, null=True)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    programa_apoyo = models.ForeignKey('programa.ListaProgramaApoyo', on_delete=models.SET_NULL, null=True)

class ProgresoAlumno(models.Model):
    anio = models.IntegerField()
    estado_aprobacion = models.CharField(max_length=50)
    curso = models.ForeignKey('academico.Curso', on_delete=models.CASCADE)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)

class NotasAlumno(models.Model):
    nota = models.FloatField()
    fecha_nota = models.DateField()
    asignatura = models.ForeignKey('academico.Asignatura', on_delete=models.CASCADE)
    curso = models.ForeignKey('academico.Curso', on_delete=models.CASCADE)
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)

class AntecedentesFamiliares(models.Model):
    nombre_padre = models.CharField(max_length=50)
    fecha_nac_padre = models.DateField()
    nombre_madre = models.CharField(max_length=50)
    fecha_nac_madre = models.DateField()
    convivientes = models.CharField(max_length=50)
    cantidad_personas_hogar = models.IntegerField(null=True)
    total_hermanos = models.IntegerField()
    posicion_familiar = models.IntegerField()

    