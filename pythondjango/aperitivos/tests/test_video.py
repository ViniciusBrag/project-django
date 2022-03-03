from model_bakery import baker
import pytest
from django.urls import reverse

from pythondjango.aperitivos.models import Video
from pythondjango.django_assertions import assert_contains

@pytest.fixture
def video(db):
    return baker.make(Video)
    

@pytest.fixture
def resp(client, video):
    resp = client.get(reverse('aperitivos:video', args=(video.slug,)))
    return resp


@pytest.fixture
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(f'{video.slug}-video_nao_existente',)))

    
def test_status_code(resp):
    assert resp.status_code == 200 


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado == 404
    
    

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}')





