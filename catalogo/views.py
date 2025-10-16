from rest_framework import viewsets
from .models import Proyecto, Alumno
from .serializers import ProyectoSerializer, AlumnoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all().order_by('-anio')
    serializer_class = ProyectoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
