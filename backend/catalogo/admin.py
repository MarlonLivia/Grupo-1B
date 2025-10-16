from django.contrib import admin
from .models import Proyecto, Alumno

class AlumnoInline(admin.TabularInline):
    model = Alumno
    extra = 1

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre_proyecto', 'anio')
    search_fields = ('nombre_proyecto', 'descripcion')
    list_filter = ('anio',)
    inlines = [AlumnoInline]

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'seccion', 'proyecto')
    search_fields = ('nombres', 'apellidos')
    list_filter = ('seccion',)
