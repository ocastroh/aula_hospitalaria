from rest_framework import serializers
from .models import TipoClase, Clase, Curso, Asignatura, Material, CalificacionDocente

class TipoClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoClase
        fields = '__all__'

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class CalificacionDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalificacionDocente
        fields = '__all__'