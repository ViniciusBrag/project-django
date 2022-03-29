import pytest
from django.urls.base import reverse
from model_bakery import baker
from pythondjango.django_assertions import assert_contains
from pythondjango.modulos.models import Aula, Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)

@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        #criação de 3 aulas
        aulas.extend(baker.make(Aula, 3, modulo=modulo))
    return aulas   

@pytest.fixture
def resp(client, modulos, aulas):
    resp = client.get(reverse('modulos:indice'))
    return resp 
    
def test_indice_disponivel(resp):
    assert resp.status_code == 200    

#def test_titulo(resp, modulo:Modulo):
 #   assert_contains(resp, modulo.titulo)
    
    
#def test_descricao(resp, modulo:Modulo):
 #   assert_contains(resp, modulo.descricao)

#def test_publico(resp, modulo:Modulo):
 #   assert_contains(resp, modulo.publico)

#def test_aulas_titulos(resp, aulas):
 #   for aula in aulas:
  #      assert_contains(resp, aula.titulo)
