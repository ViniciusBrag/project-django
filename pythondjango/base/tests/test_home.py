from django.test import Client
from django.urls import reverse
import pytest
from pythondjango.django_assertions import assert_contains

@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title> Python Pro - Home </title>')


def test_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')


def test_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')
