from django.contrib import admin
from django.urls import path, include
from . import views

app_name='login'

urlpatterns = [
    path('',views.index, name='login'),
    path('enviar',views.enviar,name='enviar'),
    path('calcular',views.calcular,name='calcular')
]
