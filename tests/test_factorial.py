import pytest
from src.factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)
