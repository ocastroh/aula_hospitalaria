from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import  Apoderado, Alumno, Coordinador, Docente
from .serializers import ApoderadoSerializer, AlumnoSerializer, CoordinadorSerializer, DocenteSerializer

@api_view(['GET', 'POST'])
def apoderado_list(request):
    if request.method == 'GET':
        apoderado = Apoderado.objects.all()
        serializer = ApoderadoSerializer(apoderado, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApoderadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def apoderado_detail(request, pk):
    try:
        apoderado = Apoderado.objects.get(pk=pk)
    except Apoderado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApoderadoSerializer(apoderado)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApoderadoSerializer(apoderado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apoderado.delete()
        return Response({"mensaje": f"Tutor ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
@api_view(['GET', 'POST'])
def alumno_list(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data)
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def alumno_detail(request, pk):
    try:
        alumno = Alumno.objects.get(pk=pk)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AlumnoSerializer(alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        alumno.delete()
        return Response({"mensaje": f"Alumno ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def coordinador_list(request):
    if request.method == 'GET':
        coordinadores = Coordinador.objects.all()
        serializer = CoordinadorSerializer(coordinadores, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoordinadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def coordinador_detail(request, pk):
    try:
        coordinador = Coordinador.objects.get(pk=pk)
    except Coordinador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoordinadorSerializer(coordinador)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoordinadorSerializer(coordinador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coordinador.delete()
        return Response({"mensaje": f"Coordinador ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def docente_list(request):
    if request.method == 'GET':
        docentes = Docente.objects.all()
        serializer = DocenteSerializer(docentes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def docente_detail(request, pk):
    try:
        docente = Docente.objects.get(pk=pk)
    except Docente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocenteSerializer(docente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocenteSerializer(docente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        docente.delete()
        return Response({"mensaje": f"Docente ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def apoderado_list(request):
    if request.method == 'GET':
        apoderados = Apoderado.objects.all()  
        serializer = ApoderadoSerializer(apoderados, many=True)  
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ApoderadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
        serializer = ApoderadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def apoderado_detail(request, pk):
    try:
        apoderado = Apoderado.objects.get(pk=pk)
    except Apoderado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApoderadoSerializer(apoderado)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApoderadoSerializer(apoderado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        apoderado.delete()
        return Response({"mensaje": f"Apoderado ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)