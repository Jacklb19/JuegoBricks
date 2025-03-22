import pytest
from src.pangrama import es_pangrama

def test_es_pangrama():
    assert es_pangrama("The quick brown fox jumps over the lazy dog") is True
    assert es_pangrama("Hola mundo") is False
