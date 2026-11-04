from .models import Vehiculo, Estacionamiento
from rest_framework import serializers

class VehiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class EstacionamientoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estacionamiento
        fields = '__all__'