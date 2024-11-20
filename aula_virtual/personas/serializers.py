from rest_framework import serializers
from .models import Alumno, Coordinador, Docente, Apoderado, Apoderado_backup
from registro.serializers import ComunaSerializer
from academico.serializers import CursoSerializer
from administrativo.serializers import SedeSerializer, AntecedentesFamiliaresSerializer

class ApoderadoSerializer(serializers.ModelSerializer):
    comuna_data = ComunaSerializer(source='comuna', read_only=True)

    class Meta:
        model = Apoderado
        fields = ['id', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno', 
                 'direccion', 'comuna', 'comuna_data', 'email', 'telefono', 
                 'parentezco', 'fecha_nacimiento']
        extra_kwargs = {'comuna': {'write_only': True}}

class ApoderadoBackupSerializer(serializers.ModelSerializer):
    comuna_data = ComunaSerializer(source='comuna', read_only=True)

    class Meta:
        model = Apoderado_backup
        fields = ['id', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno', 
                 'direccion', 'comuna', 'comuna_data', 'email', 'telefono', 
                 'parentezco', 'fecha_nacimiento']
        extra_kwargs = {'comuna': {'write_only': True}}

class AlumnoSerializer(serializers.ModelSerializer):
    comuna_data = ComunaSerializer(source='comuna', read_only=True)
    apoderado_data = ApoderadoSerializer(source='apoderado', read_only=True)
    apoderado_backup_data = ApoderadoBackupSerializer(source='apoderado_backup', read_only=True)
    curso_data = CursoSerializer(source='curso', read_only=True)
    antecedentes_familiares = AntecedentesFamiliaresSerializer(read_only=True)    
    class Meta:
        model = Alumno
        fields = ['id', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno',
                 'direccion', 'comuna', 'comuna_data', 'email', 'telefono',
                 'fecha_nacimiento', 'colegio_origen', 'apoderado', 'apoderado_data',
                    'apoderado_backup', 'apoderado_backup_data',
                 'curso', 'curso_data', 'identificador_curso', 'antecedentes_familiares']
        extra_kwargs = {
            'comuna': {'write_only': True},
            'apoderado': {'write_only': True},
            'apoderado_backup': {'write_only': True},
            'curso': {'write_only': True},
            'antecedentes_familiares': {'write_only': True}
        }

class CoordinadorSerializer(serializers.ModelSerializer):
    comuna_data = ComunaSerializer(source='comuna', read_only=True)

    class Meta:
        model = Coordinador
        fields = ['id', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno',
                 'direccion', 'comuna', 'comuna_data', 'email', 'telefono', 'fecha_nacimiento']
        extra_kwargs = {'comuna': {'write_only': True}}

class DocenteSerializer(serializers.ModelSerializer):
    comuna_data = ComunaSerializer(source='comuna', read_only=True)
    sede_data = SedeSerializer(source='sede', read_only=True)
    
    class Meta:
        model = Docente
        fields = ['id', 'rut', 'nombres', 'apellido_paterno', 'apellido_materno',
                 'direccion', 'comuna', 'comuna_data', 'email', 'telefono', 
                 'fecha_nacimiento', 'sede', 'sede_data']
        extra_kwargs = {
            'comuna': {'write_only': True},
            'sede': {'write_only': True}
        }
