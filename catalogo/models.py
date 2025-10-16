from django.db import models

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True, null=True)
    anio = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.nombre_proyecto} ({self.anio})"


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    seccion = models.CharField(max_length=5, blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='alumnos')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
