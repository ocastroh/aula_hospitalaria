from rest_framework import serializers
from .models import ListaProgramaApoyo, HojaDeVida

class ListaProgramaApoyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaProgramaApoyo
        fields = '__all__'

class HojaDeVidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HojaDeVida
        fields = '__all__'



