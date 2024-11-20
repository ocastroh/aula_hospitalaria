from django.db import models

class MotivoClase(models.Model):
    descripcion_motivo = models.TextField()

class RegistroClase(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    tipo_clase = models.ForeignKey('academico.TipoClase', on_delete=models.CASCADE)
    calificacion_docente = models.ForeignKey('academico.CalificacionDocente', on_delete=models.SET_NULL, null=True)
    motivo_cierre = models.ForeignKey(MotivoClase, on_delete=models.SET_NULL, null=True)
    hr_inicio_efectivo = models.TimeField(default="00:00")  # formato correcto
    hr_termino_efectivo = models.TimeField(default="00:00")
    registro_asignatura = models.ForeignKey('RegistroAsignatura', on_delete=models.SET_NULL, null=True)
    
    
    
    
class RegistroAsignatura(models.Model):
    alumno = models.ForeignKey('personas.Alumno', on_delete=models.CASCADE)
    docente = models.ForeignKey('personas.Docente', on_delete=models.SET_NULL, null=True)
    asignatura = models.ForeignKey('academico.Asignatura', on_delete=models.CASCADE)


class Comuna(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)

   
class Region(models.Model):
    nombre = models.CharField(max_length=200)

  
class ListaHorarioBloque(models.Model):
    numero_bloque = models.IntegerField()
    hr_inicio_programado = models.TimeField()
    hr_termino_programado = models.TimeField()
  
    
class Bloque(models.Model):
     dia = models.CharField(max_length=20)
     registro_asignatura = models.ForeignKey('RegistroAsignatura', on_delete=models.CASCADE)
     lista_horario_bloque = models.ForeignKey('ListaHorarioBloque', on_delete=models.CASCADE)
    
    
    

    
    
class CoordinadorSede(models.Model):
    sede = models.ForeignKey('administrativo.Sede', on_delete=models.SET_NULL, null=True)
    coordinador = models.ForeignKey('personas.Coordinador', on_delete=models.CASCADE)
    
    
    
    
