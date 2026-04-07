"""Unit tests for calculator module."""

import pytest

from calculator import add, divide, multiply, subtract


def test_add_positive_numbers() -> None:
    assert add(2, 3) == 5


def test_subtract_positive_numbers() -> None:
    assert subtract(10, 4) == 6


def test_multiply_positive_numbers() -> None:
    assert multiply(6, 7) == 42


def test_divide_positive_numbers() -> None:
    assert divide(12, 3) == 4


def test_divide_by_zero_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide(10, 0)


def test_add_negative_numbers() -> None:
    assert add(-2, -8) == -10
