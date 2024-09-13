"""
This module contains unit tests for the Calculator class.
"""

import pytest
from calculator.calculator_logic import Calculator


@pytest.fixture
def calculator():
    """Fixture to create a Calculator object before each test."""
    return Calculator()


def test_add(calculator: Calculator):
    """
    Test the add() method of the Calculator class.

    Parameters:
    calculator (Calculator): The Calculator object.
    """
    assert calculator.add(-5) == -5
    assert calculator.add(10.5) == 5.5


def test_subtract(calculator: Calculator):
    """
    Test the subtract() method of the Calculator class.

    Parameters:
    calculator (Calculator): The Calculator object.
    """
    calculator.add(10)
    assert calculator.subtract(3) == 7
    assert calculator.subtract(2) == 5
    assert calculator.subtract(10) == -5


def test_multiply(calculator: Calculator):
    """
    Test the multiply() method of the Calculator class.

    Parameters:
    calculator (Calculator): The Calculator object.
    """
    calculator.add(5)
    assert calculator.multiply(2.5) == 12.5
    assert calculator.multiply(0) == 0


def test_divide(calculator: Calculator):
    """
    Test the divide() method of the Calculator class.

    Parameters:
    calculator (Calculator): The Calculator object.
    """
    calculator.add(20)
    assert calculator.divide(2) == 10
    assert calculator.divide(5) == 2
    with pytest.raises(ValueError):
        calculator.divide(0)


def test_nth_root(calculator: Calculator):
    """
    Test the nth_root() method of the Calculator class.

    Parameters:
    calculator (Calculator): The Calculator object.
    """
    calculator.add(16)
    assert calculator.nth_root(4) == 2
    with pytest.raises(ValueError):
        calculator.nth_root(0)


def test_reset_memory(calculator: Calculator):
    """
    Test the reset_memory() method of the Calculator class.

    Parameters:
        calculator (Calculator): The Calculator object.
    """
    calculator.add(10)
    calculator.reset_memory()
    assert calculator.memory == 0


if __name__ == "__main__":
    pytest.main()
