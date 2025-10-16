from rest_framework import serializers
from .models import Proyecto, Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'nombres', 'apellidos', 'seccion']

class ProyectoSerializer(serializers.ModelSerializer):
    alumnos = AlumnoSerializer(many=True, read_only=True)

    class Meta:
        model = Proyecto
        fields = ['id_proyecto', 'nombre_proyecto', 'descripcion', 'anio', 'alumnos']
