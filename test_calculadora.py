
import pytest
from calculadora import dividir


def test_division_normal():
    assert dividir(10, 2) == 5


def test_division_con_decimal():
    assert dividir(7, 2) == 3.5


def test_division_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
