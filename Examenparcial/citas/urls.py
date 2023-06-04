from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import (home,documentoList,documentoCreate,documentoUpdate,documentoDelete,seguroList,seguroCreate,seguroUpdate,seguroDelete,pacienteList,pacienteCreate,pacienteUpdate,pacienteDelete,especialidadesList,especialidadesCreate,especialidadesUpdate,especialidadesDelete)

urlpatterns = [
    path('', home, name='home'),
    path("tipodocumento/", documentoList.as_view(),name="tipodocumento"),
    path("tipodocumento/create/", documentoCreate.as_view(), name="tipodocumento-create"),
    path("tipodocumento/update/<int:pk>/",documentoUpdate.as_view(),name="tipodocumento-update"),
    path("tipodocumento/delete/<int:pk>/",documentoDelete.as_view(),name="tipodocumento-delete"),
    
    path("tiposeguro/", seguroList.as_view(),name="tiposeguro"),
    path("tiposeguro/create/", seguroCreate.as_view(), name="tiposeguro-create"),
    path("tiposeguro/update/<int:pk>/",seguroUpdate.as_view(),name="tiposeguro-update"),
    path("tiposeguro/delete/<int:pk>/",seguroDelete.as_view(),name="tiposeguro-delete"),
    
    path("paciente/", pacienteList.as_view(),name="paciente"),
    path("paciente/create/", pacienteCreate.as_view(), name="paciente-create"),
    path("paciente/update/<int:pk>/",pacienteUpdate.as_view(),name="paciente-update"),
    path("paciente/delete/<int:pk>/", pacienteDelete.as_view(),name="paciente-delete"),
    
    path("especialidades/", especialidadesList.as_view(), name="especialidades"),
    path("especialidades/create/",especialidadesCreate.as_view(),name="especialidades-create"),
    path("especialidades/update/<int:pk>/",especialidadesUpdate.as_view(),name="especialidades-update"),
    path("especialidades/delete/<int:pk>/",especialidadesDelete.as_view(),name="especialidades-delete",),
]