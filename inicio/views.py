from django.shortcuts import render
from rest_framework import generics
from .models import Vehiculo, Estacionamiento, Reserva
from .serializers import VehiculoSerializer, EstacionamientoSerializer, ReservaSerializer


#Para vehiculos
class VehiculoListView(generics.ListCreateAPIView):
    
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


#Para Estacionamiento
class EstacionamientoListView(generics.ListCreateAPIView):
    
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer

class EstacionamientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Estacionamiento.objects.all()
    serializer_class = EstacionamientoSerializer
    
#Para Reservas
class ReservaListView(generics.ListCreateAPIView):
    
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer