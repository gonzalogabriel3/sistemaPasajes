from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agente', views.indexAgenteView, name='agente'),
    path('localidad', views.indexLocalidadView, name='localidad'),
    path('familiar', views.indexFamiliarView, name='familiar'),
    path('empresa', views.indexEmpresaView, name='empresa'),
    path('pasaje', views.indexPasajeView, name='pasaje'),

    ####Formularios#####
    path('abmAgente', views.abmAgente, name='abmAgente'),


]
