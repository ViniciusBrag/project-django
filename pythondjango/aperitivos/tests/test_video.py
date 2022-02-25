from django.urls import reverse
import pytest
from pythondjango.django_assertions import assert_contains
from pythondjango.aperitivos.views import Video

@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug, ))) 

def test_status_code(resp):
   assert resp.status_code == 200


def test_contexto_video(resp):
    assert_contains(resp, 'iframe src="https://player.vimeo.com/video/251224475')    

def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)