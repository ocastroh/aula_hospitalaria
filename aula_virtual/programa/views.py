from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ListaProgramaApoyo, HojaDeVida
from .serializers import ListaProgramaApoyoSerializer, HojaDeVidaSerializer

@api_view(['GET', 'POST'])
def programa_list(request):
    if request.method == 'GET':
        programas = ListaProgramaApoyo.objects.all()
        serializer = ListaProgramaApoyoSerializer(programas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ListaProgramaApoyoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def programa_detail(request, pk):
    try:
        programa = ListaProgramaApoyo.objects.get(pk=pk)
    except Programa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListaProgramaApoyoSerializer(programa)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ListaProgramaApoyoSerializer(programa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        programa.delete()
        return Response({"mensaje": f"Programa ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def hoja_de_vida_list(request):
    if request.method == 'GET':
        hojas_de_vida = HojaDeVida.objects.all()
        serializer = HojaDeVidaSerializer(hojas_de_vida, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = HojaDeVidaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def hoja_de_vida_detail(request, pk):
    try:
        hoja_de_vida = HojaDeVida.objects.get(pk=pk)
    except HojaDeVida.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HojaDeVidaSerializer(hoja_de_vida)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = HojaDeVidaSerializer(hoja_de_vida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        hoja_de_vida.delete()
        return Response({"mensaje": f"HojaDeVida ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
    