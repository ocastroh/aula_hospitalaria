from rest_framework import serializers
from .models import Sede, Matricula, ProgresoAlumno, NotasAlumno, AntecedentesFamiliares
from personas.models import Apoderado, Alumno
from programa.models import ListaProgramaApoyo
from academico.models import Curso
from programa.serializers import ListaProgramaApoyoSerializer

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ProgresoAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoAlumno
        fields = '__all__'

class NotasAlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasAlumno
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    alumno = serializers.PrimaryKeyRelatedField(queryset=Alumno.objects.all())
    sede = SedeSerializer()
    programa_apoyo = ListaProgramaApoyoSerializer()

    class Meta:
        model = Matricula
        fields = ['folio', 'fecha', 'observaciones', 'sede', 'alumno', 'programa_apoyo']

    def create(self, validated_data):
        sede_data = validated_data.pop('sede')
        programa_data = validated_data.pop('programa_apoyo')

        # Crear o recuperar la sede
        sede, _ = Sede.objects.get_or_create(**sede_data)

        # Crear o recuperar el programa de apoyo
        programa, _ = ListaProgramaApoyo.objects.get_or_create(**programa_data)

        # Obtener el alumno existente
        alumno = validated_data.pop('alumno')

        # Crear la matrícula
        matricula = Matricula.objects.create(
            folio=validated_data['folio'],
            fecha=validated_data['fecha'],
            observaciones=validated_data['observaciones'],
            sede=sede,
            alumno=alumno,
            programa_apoyo=programa
        )

        return matricula

    def update(self, instance, validated_data):
        sede_data = validated_data.pop('sede', None)
        programa_data = validated_data.pop('programa_apoyo', None)

        # Actualizar campos simples
        instance.folio = validated_data.get('folio', instance.folio)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.observaciones = validated_data.get('observaciones', instance.observaciones)

        # Actualizar o crear la sede si se proporciona
        if sede_data:
            sede, _ = Sede.objects.get_or_create(**sede_data)
            instance.sede = sede

        # Actualizar o crear el programa de apoyo si se proporciona
        if programa_data:
            programa, _ = ListaProgramaApoyo.objects.get_or_create(**programa_data)
            instance.programa_apoyo = programa

        # Actualizar el alumno si cambia
        alumno = validated_data.get('alumno')
        if alumno:
            instance.alumno = alumno

        # Guardar la instancia actualizada
        instance.save()
        return instance

class AntecedentesFamiliaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = AntecedentesFamiliares
        fields = '__all__'