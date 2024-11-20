from django.urls import path
from . import views 

urlpatterns = [
    path('motivos-clase/', views.motivo_clase_list, name='motivo-clase-list'),
    path('motivos-clase/<int:pk>/', views.motivo_clase_detail, name='motivo-clase-detail'),
    path('registros-clase/', views.registro_clase_list, name='registro-clase-list'),
    path('registros-clase/<int:pk>/', views.registro_clase_detail, name='registro-clase-detail'),
    path('regiones/', views.region_list, name='region-list'),
    path('regiones/<int:pk>/', views.region_detail, name='region-detail'),
    path('comunas/', views.comuna_list, name='comuna-list'),
    path('comunas/<int:pk>/', views.comuna_detail, name='comuna-detail'),
    
]
