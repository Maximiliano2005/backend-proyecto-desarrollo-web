from .models import Vehiculo, Estacionamiento, Reserva
from rest_framework import serializers

class VehiculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehiculo
        fields = '__all__'
        
class EstacionamientoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estacionamiento
        fields = '__all__'
        
class ReservaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reserva
        fields = '__all__'
        
    def validate(self, attrs):
        inicio = attrs.get("fecha_inicio")
        fin = attrs.get("fecha_fin")
        
        
        if (fin <= inicio):
            raise serializers.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio")
        return attrs
    
    