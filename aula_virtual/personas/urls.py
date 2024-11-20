from django.urls import path
from . import views

urlpatterns = [
    path('apoderados/', views.apoderado_list, name='apoderado-list'),
    path('apoderados/<int:pk>/', views.apoderado_detail, name='apoderado-detail'),
    path('alumnos/', views.alumno_list, name='alumno-list'),
    path('alumnos/<int:pk>/', views.alumno_detail, name='alumno-detail'),
    path('coordinadores/', views.coordinador_list, name='coordinador-list'),
    path('coordinadores/<int:pk>/', views.coordinador_detail, name='coordinador-detail'),
    path('docentes/', views.docente_list, name='docente-list'),
    path('docentes/<int:pk>/', views.docente_detail, name='docente-detail'),
]
