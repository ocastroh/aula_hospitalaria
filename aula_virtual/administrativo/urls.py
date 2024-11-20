from django.urls import path
from . import views

urlpatterns = [
    path('sedes/', views.sede_list, name='sede-list'),
    path('sedes/<int:pk>/', views.sede_detail, name='sede-detail'),
    path('matriculas/', views.matricula_list, name='matricula-list'),
    path('matriculas/<int:pk>/', views.matricula_detail, name='matricula-detail'),
    path('progresos/', views.progreso_alumno_list, name='progreso-alumno-list'),
    path('progresos/<int:pk>/', views.progreso_alumno_detail, name='progreso-alumno-detail'),
    path('notas/', views.notas_alumno_list, name='notas-alumno-list'),
    path('notas/<int:pk>/', views.notas_alumno_detail, name='notas-alumno-detail'),
]