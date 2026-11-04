from django.shortcuts import render
from rest_framework import generics
from .models import Vehiculo, Estacionamiento
from .serializers import VehiculoSerializer, EstacionamientoSerializer


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