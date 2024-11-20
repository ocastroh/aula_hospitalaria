from django.urls import path
from . import views

urlpatterns = [
    path('tipos-clase/', views.tipo_clase_list, name='tipo-clase-list'),
    path('tipos-clase/<int:pk>/', views.tipo_clase_detail, name='tipo-clase-detail'),
    path('clases/', views.clase_list, name='clase-list'),
    path('clases/<int:pk>/', views.clase_detail, name='clase-detail'),
    path('cursos/', views.curso_list, name='curso-list'),
    path('cursos/<int:pk>/', views.curso_detail, name='curso-detail'),
    path('asignaturas/', views.asignatura_list, name='asignatura-list'),
    path('asignaturas/<int:pk>/', views.asignatura_detail, name='asignatura-detail'),
    path('materiales/', views.material_list, name='material-list'),
    path('materiales/<int:pk>/', views.material_detail, name='material-detail'),
    path('calificaciones-docente/', views.calificacion_docente_list, name='calificacion-docente-list'),
    path('calificaciones-docente/<int:pk>/', views.calificacion_docente_detail, name='calificacion-docente-detail'),
]
