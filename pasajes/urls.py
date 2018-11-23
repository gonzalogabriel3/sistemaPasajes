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

    #**ABM Agente**#
    path('altaAgente', views.altaAgente, name='altaAgente'),
    path('modificacionAgente/<int:idAgente>/', views.modificacionAgente, name='modificacionAgente'),
    path('bajaAgente/<int:idAgente>/', views.bajaAgente, name='bajaAgente'),

    #**ABM Localidad**#
    path('altaLocalidad', views.altaLocalidad, name='altaAgente'),
    path('bajaLocalidad/<int:idLocalidad>/', views.bajaLocalidad, name='bajaLocalidad'),
    path('modificacionLocalidad/<int:idLocalidad>/', views.modificacionLocalidad, name='modificacionLocalidad'),

    #**ABM Familiar**#
    path('altaFamiliar', views.altaFamiliar, name='altaFamiliar'),
    path('bajaFamiliar/<int:idFamiliar>/', views.bajaFamiliar, name='bajaFamiliar'),
    path('modificacionFamiliar/<int:idFamiliar>/', views.modificacionFamiliar, name='modificacionFamiliar'),

    #**ABM Empresa**#
    path('altaEmpresa', views.altaEmpresa, name='altaEmpresa'),
    path('bajaEmpresa/<int:idEmpresa>/', views.bajaEmpresa, name='bajaEmpresa'),
    path('modificacionEmpresa/<int:idEmpresa>/', views.modificacionEmpresa, name='modificacionEmpresa'),


]
