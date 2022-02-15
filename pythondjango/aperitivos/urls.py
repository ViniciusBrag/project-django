from django.urls import path

from pythondjango.aperitivos.views import indice, video

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='motivacao'),
    path('', indice, name='indice'),
]