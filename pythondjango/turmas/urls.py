from django import views
from django.urls import path
from pythondjango.turmas import views

app_name = 'turmas'

urlpatterns = [
    path('', views.indice, name='indice'),
]
