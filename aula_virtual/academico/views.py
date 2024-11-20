from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TipoClase, Clase, Curso, Asignatura, Material, CalificacionDocente
from .serializers import TipoClaseSerializer, ClaseSerializer, CursoSerializer, AsignaturaSerializer, MaterialSerializer, CalificacionDocenteSerializer

@api_view(['GET', 'POST'])
def tipo_clase_list(request):
    if request.method == 'GET':
        tipos_clase = TipoClase.objects.all()
        serializer = TipoClaseSerializer(tipos_clase, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TipoClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tipo_clase_detail(request, pk):
    try:
        tipo_clase = TipoClase.objects.get(pk=pk)
    except TipoClase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoClaseSerializer(tipo_clase)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TipoClaseSerializer(tipo_clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tipo_clase.delete()
        return Response({"mensaje": f"TipoClase ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def clase_list(request):
    if request.method == 'GET':
        clases = Clase.objects.all()
        serializer = ClaseSerializer(clases, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def clase_detail(request, pk):
    try:
        clase = Clase.objects.get(pk=pk)
    except Clase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClaseSerializer(clase)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ClaseSerializer(clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        clase.delete()
        return Response({"mensaje": f"Clase ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def curso_list(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def curso_detail(request, pk):
    try:
        curso = Curso.objects.get(pk=pk)
    except Curso.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CursoSerializer(curso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        curso.delete()
        return Response({"mensaje": f"Curso ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def asignatura_list(request):
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        serializer = AsignaturaSerializer(asignaturas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def asignatura_detail(request, pk):
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AsignaturaSerializer(asignatura)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AsignaturaSerializer(asignatura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        asignatura.delete()
        return Response({"mensaje": f"Asignatura ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def material_list(request):
    if request.method == 'GET':
        materiales = Material.objects.all()
        serializer = MaterialSerializer(materiales, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def material_detail(request, pk):
    try:
        material = Material.objects.get(pk=pk)
    except Material.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MaterialSerializer(material)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        material.delete()
        return Response({"mensaje": f"Material ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def calificacion_docente_list(request):
    if request.method == 'GET':
        calificaciones = CalificacionDocente.objects.all()
        serializer = CalificacionDocenteSerializer(calificaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CalificacionDocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def calificacion_docente_detail(request, pk):
    try:
        calificacion = CalificacionDocente.objects.get(pk=pk)
    except CalificacionDocente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CalificacionDocenteSerializer(calificacion)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CalificacionDocenteSerializer(calificacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        calificacion.delete()
        return Response({"mensaje": f"CalificacionDocente ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)