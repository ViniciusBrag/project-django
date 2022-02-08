from django.urls import path

from pythondjango.aperitivos.views import video

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]