from model_mommy import mommy
import pytest
from django.urls import reverse
from pythondjango.aperitivos.models import Video
from pythondjango.django_assertions import assert_contains

@pytest.fixture
def video(db):
    return mommy.make(Video)
    

@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))

@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug+'video_nao_existente',)))

    
def test_status_code(resp):
    assert resp.status_code == 200 


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado == 404
    
    

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<div style="padding:59.41% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/{video.vimeo_id}?h=2ede6adb1b&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="y2metacom-Python Birds - Programa&amp;ccedil;&amp;atilde;o Orientada a Objetos-(480p)"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>"')





