from django.urls import path
from .views import VehiculoListView, VehiculoDetailView, EstacionamientoListView, EstacionamientoDetailView

urlpatterns = [
    path('vehiculos/', VehiculoListView.as_view(), name='lista-vehiculos'),
    path("vehiculos/<int:pk>/", VehiculoDetailView.as_view(), name="detalle-vehiculo"),
    path('estacionamientos/', EstacionamientoListView.as_view(), name='lista-estacionamiento'),
    path("estacionamientos/<int:pk>/", EstacionamientoDetailView.as_view(), name="detalle-estacionamiento"),
]
