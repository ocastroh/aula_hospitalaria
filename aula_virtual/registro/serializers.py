from rest_framework import serializers
from .models import Comuna, Region, MotivoClase, RegistroClase, RegistroAsignatura

from academico.serializers import *

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    region_data = RegionSerializer(source='region', read_only=True)
    
    class Meta:
        model = Comuna
        fields = ['id', 'nombre', 'region', 'region_data']
        extra_kwargs = {'region': {'write_only': True}}

class MotivoClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoClase
        fields = '__all__'

class RegistroClaseSerializer(serializers.ModelSerializer):
    tipo_clase_data = TipoClaseSerializer(source='tipo_clase', read_only=True)
    calificacion_docente_data = CalificacionDocenteSerializer(source='calificacion_docente', read_only=True)
    motivo_cierre_data = MotivoClaseSerializer(source='motivo_cierre', read_only=True)
    
    class Meta:
        model = RegistroClase
        fields = ['id', 'fecha_registro', 'tipo_clase', 'tipo_clase_data', 'calificacion_docente', 
                  'calificacion_docente_data', 'motivo_cierre', 'motivo_cierre_data', 'hr_inicio_efectivo',
                  'hr_termino_efectivo', 'registro_asignatura']
        extra_kwargs = {
            'tipo_clase': {'write_only': True},
            'calificacion_docente': {'write_only': True},
            'motivo_cierre': {'write_only': True}
        }

class RegistroAsignaturaSerializer(serializers.ModelSerializer):
    alumno_data = serializers.SerializerMethodField()
    docente_data = serializers.SerializerMethodField()
    asignatura_data = serializers.SerializerMethodField()

    def get_alumno_data(self, obj):
        from personas.serializers import AlumnoSerializer
        return AlumnoSerializer(obj.alumno).data

    def get_docente_data(self, obj):
        from personas.serializers import DocenteSerializer
        return DocenteSerializer(obj.docente).data

    def get_asignatura_data(self, obj):
        from academico.serializers import AsignaturaSerializer
        return AsignaturaSerializer(obj.asignatura).data

    class Meta:
        model = RegistroAsignatura
        fields = ['id', 'alumno', 'alumno_data', 'docente', 'docente_data', 'asignatura', 'asignatura_data']
        extra_kwargs = {
            'alumno': {'write_only': True},
            'docente': {'write_only': True},
            'asignatura': {'write_only': True}
        }
