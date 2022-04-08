import pytest
from django.urls.base import reverse
from model_bakery import baker
from pythondjango.django_assertions import assert_contains
from pythondjango.modulos.models import Aula, Modulo
from pythondjango.conftest import client_com_usuario_logado


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)

@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)

@pytest.fixture
def resp(client_com_usuario_logado, aula):
    resp = client_com_usuario_logado.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp 
    

def test_titulo_aula(resp, aula: Aula):
    assert_contains(resp, aula.titulo)
    
    
def test_vimeo(resp, aula: Aula):
    assert_contains(resp, f'src="https://player.vimeo.com/video/{ aula.vimeo_id }"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp,   f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}</a></li>')



@pytest.fixture
def resp_sem_usuario(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_usuario_nao_logado_redirect(resp_sem_usuario):
    """
    Função para certificar que o usuario vai ser rediricionado para o login do app.

    Args:
        resp_sem_usuario (_type_): Função para certificar que não tem nenhum usuário logado
    """
    assert resp_sem_usuario.status_code == 302
    assert resp_sem_usuario.url.startswith(reverse('login'))



