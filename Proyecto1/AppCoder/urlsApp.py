
from django.urls import path
from AppCoder import vistas

urlpatterns = [
    
    path("", views.inicio),
    path("cursos", views.cursos, name="Cursos"),
    path("Profesor", views.cursos, name="Profesor"),
    path("Estudiante", views.cursos, name="Estudiante")
     
]