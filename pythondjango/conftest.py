import pytest
from model_bakery import baker


@pytest.fixture
def usuario_logado(db, django_user_model):
    """
    Criação de usuário logado        
    Args:
        db (banco de dados): para acessar o banco de dados
        django_user_model (modelo de usuário do django): 
        Modulo para acessar o usuário do próprio django 

    Returns:
        Retorna o usuário criado dentro do banco de dados
    """
    usuario_modelo_criado = baker.make(django_user_model, first_name='Fulano')
    return usuario_modelo_criado 

@pytest.fixture
def client_com_usuario_logado(usuario_logado, client):
    """
    Fixture que simula o efeito de usuário logando no site
    Args:
        usuario_logado (fixture): criação de usuário logado
        Client (método do módulo client):Classe do python que atua como um navegador web fictício para acessar e interajir com as views.

    Returns:
        Retornar um usuário logado na app.
    """
    client.force_login(usuario_logado)
    return client

