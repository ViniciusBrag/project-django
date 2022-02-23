from msilib.schema import Class
from multiprocessing import context
from urllib import response
from django.shortcuts import render
from aperitivos.models import Video


videos = [
        Video(slug='motivacao', titulo = 'Video Aperitivo: Motivação', vimeo_id='675270281'),
        Video(slug='instalacao-windows', titulo = 'Instalação-windows', vimeo_id='251497668'),
]

videos_dct = {v.slug: v for v in videos}

def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})

def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

