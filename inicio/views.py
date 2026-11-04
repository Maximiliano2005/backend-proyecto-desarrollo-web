from django.shortcuts import render
from rest_framework import generics
from .models import Vehiculo
from .serializers import VehiculoSerializer

class VehiculoListView(generics.ListAPIView):
    
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

# Create your views here.
