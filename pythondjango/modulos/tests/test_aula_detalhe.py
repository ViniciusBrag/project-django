import pytest
from django.urls.base import reverse
from model_bakery import baker
from pythondjango.django_assertions import assert_contains
from pythondjango.modulos.models import Aula, Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)

@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)

@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp 
    

def test_titulo_aula(resp, aula: Aula):
    assert_contains(resp, aula.titulo)
    
    
def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp,   f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')


