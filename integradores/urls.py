from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalogo.views import ProyectoViewSet, AlumnoViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
