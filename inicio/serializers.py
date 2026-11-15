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
        inicio = attrs.get("fecha_inicio", self.instance.fecha_inicio if self.instance else None)
        fin = attrs.get("fecha_fin", self.instance.fecha_fin if self.instance else None)
        estacionamiento = attrs.get("estacionamiento", self.instance.estacionamiento if self.instance else None)
        
        
        if (fin <= inicio):
            raise serializers.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio")
        
        reservas = Reserva.objects.filter(
            estacionamiento = estacionamiento,
            fecha_inicio__lt= fin,
            fecha_fin__gt= inicio
        ).exclude(estado="cancelada")
        
        if self.instance:
            reservas = reservas.exclude(pk=self.instance.pk)
        
        if reservas.exists():
            raise serializers.ValidationError(
                "El estacionamiento ya esta reservado en ese horario"
            )
        return attrs
    
    