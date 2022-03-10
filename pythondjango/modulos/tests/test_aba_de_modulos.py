import pytest
from django.urls.base import reverse
from model_bakery import baker
from pythondjango.django_assertions import assert_contains
from pythondjango.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def resp(client, modulos):
    resp = client.get(reverse('base:home'))
    return resp 
    

def test_titulo_modulos(resp, modulos):
    for modulo in modulos:
        assert_contains(resp, modulo.titulo)
    
    
