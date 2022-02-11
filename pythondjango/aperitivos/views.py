from multiprocessing import context
from django.shortcuts import render

def video(request, slug):
    videos= {
        'motivacao':{'titulo': 'Video Aperitivo: Motivação', 'vimeo_id':675270281},
        'instalacao-windows':{'titulo': 'Instalação-windows', 'vimeo_id':251497668},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

