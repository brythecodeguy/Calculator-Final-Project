# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide, power, modulus, calculate  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'power' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),            # Test exponentiation with positive integers
        (5, 0, 1),            # Test any number raised to zero
        (4, 0.5, 2.0),        # Test fractional exponent
        (-2, 3, -8),          # Test negative base with odd exponent
    ],
    ids=[
        "power_positive_integers",
        "power_zero_exponent",
        "power_fractional_exponent",
        "power_negative_base_odd_exponent",
    ]
)
def test_power(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'power' function with integers and floats.
    """
    result = power(a, b)

    assert result == expected, f"Expected power({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'modulus' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 1),           # Test positive integer remainder
        (10, 5, 0),           # Test evenly divisible numbers
        (10.5, 4, 2.5),       # Test float dividend
        (-10, 3, 2),          # Test Python modulus behavior with negative dividend
    ],
    ids=[
        "modulus_positive_integers",
        "modulus_evenly_divisible",
        "modulus_float_dividend",
        "modulus_negative_dividend",
    ]
)
def test_modulus(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'modulus' function with integers and floats.
    """
    result = modulus(a, b)

    assert result == expected, f"Expected modulus({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Modulus by Zero
# ---------------------------------------------

def test_modulus_by_zero() -> None:
    """
    Test the 'modulus' function with modulus by zero.
    """
    with pytest.raises(ValueError) as excinfo:
        modulus(10, 0)

    assert "Cannot calculate modulus by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot calculate modulus by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Tests for the 'calculate' Dispatcher
# ---------------------------------------------

@pytest.mark.parametrize(
    "operation_type, a, b, expected",
    [
        ("addition", 10, 5, 15),
        ("subtraction", 10, 5, 5),
        ("multiplication", 10, 5, 50),
        ("division", 20, 4, 5),
        ("power", 2, 3, 8),
        ("modulus", 10, 3, 1),
    ],
    ids=[
        "calculate_addition",
        "calculate_subtraction",
        "calculate_multiplication",
        "calculate_division",
        "calculate_power",
        "calculate_modulus",
    ]
)
def test_calculate_dispatch(operation_type: str, a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'calculate' dispatcher routes operation types to the correct function.
    """
    result = calculate(operation_type, a, b)

    assert result == expected, (
        f"Expected calculate({operation_type}, {a}, {b}) to be {expected}, but got {result}"
    )


def test_calculate_invalid_operation_type() -> None:
    """
    Test the 'calculate' dispatcher with an unsupported operation type.
    """
    with pytest.raises(ValueError) as excinfo:
        calculate("square_root", 10, 2)

    assert "Unsupported calculation type: square_root" in str(excinfo.value), \
        f"Expected unsupported calculation type error, but got '{excinfo.value}'"
