from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:agente_id>/', views.agente, name='showAgente'),
    path('agente', views.indexAgente, name='agente'),
    path('agente2', views.indexAgente2, name='agente2'),
]
