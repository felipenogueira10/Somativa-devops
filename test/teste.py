import random

from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World"}

def funcaoteste(true=None):
    with patch('random.randint' , return_value=12345)
        result = funcaoteste()

    assert result() == {"teste": true, "num_aleatorio": 12345}

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    assert estudante_teste == create_estudante()

def test_update_estudante_negativo():
    assert not update_estudante(-5)  # Testa ID negativo

def test_update_estudante_positivo():
    assert update_estudante(10)
    # Testa ID positivo

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)

def test_delete_estudante_positivo():
        assert delete_estudante(-5)

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool