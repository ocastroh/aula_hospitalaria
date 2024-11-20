from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MotivoClase, RegistroClase, Region, Comuna
from .serializers import MotivoClaseSerializer, RegistroClaseSerializer, RegionSerializer, ComunaSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def motivo_clase_list(request):
    if request.method == 'GET':
        motivos = MotivoClase.objects.all()
        serializer = MotivoClaseSerializer(motivos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MotivoClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def motivo_clase_detail(request, pk):
    try:
        motivo = MotivoClase.objects.get(pk=pk)
    except MotivoClase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MotivoClaseSerializer(motivo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MotivoClaseSerializer(motivo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        motivo.delete()
        return Response({"mensaje": f"MotivoClase ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def registro_clase_list(request):
    if request.method == 'GET':
        registros = RegistroClase.objects.all()
        serializer = RegistroClaseSerializer(registros, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegistroClaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def registro_clase_detail(request, pk):
    try:
        registro = RegistroClase.objects.get(pk=pk)
    except RegistroClase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroClaseSerializer(registro)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RegistroClaseSerializer(registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        registro.delete()
        return Response({"mensaje": f"RegistroClase ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
    
    
@api_view(['GET', 'POST'])
def region_list(request):
    if request.method == 'GET':
        regiones = Region.objects.all()
        serializer = RegionSerializer(regiones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk):
    try:
        region = Region.objects.get(pk=pk)
    except Region.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        region.delete()
        return Response({"mensaje": f"Region ID: {pk} ha sido eliminada correctamente"}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def comuna_list(request):
    if request.method == 'GET':
        comunas = Comuna.objects.all()
        serializer = ComunaSerializer(comunas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def comuna_detail(request, pk):
    try:
        comuna = Comuna.objects.get(pk=pk)
    except Comuna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComunaSerializer(comuna)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ComunaSerializer(comuna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comuna.delete()
        return Response({"mensaje": f"Comuna ID: {pk} ha sido eliminada correctamente"}, status=status.HTTP_200_OK)
